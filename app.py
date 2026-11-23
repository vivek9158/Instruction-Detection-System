import os, io, joblib, pandas as pd
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")
FILES = ["ids_random_forest_model.pkl", "ids_label_encoder.pkl",
         "ids_feature_columns.pkl", "ids_input_columns.pkl",
         "ids_categorical_columns.pkl"]

try:
    model, encoder, encoded_cols, input_cols, categorical_cols = [
        joblib.load(os.path.join(os.path.dirname(__file__), f)) for f in FILES
    ]
    encoded_cols, input_cols, categorical_cols = list(encoded_cols), list(input_cols), list(categorical_cols)
    assert len(encoded_cols) == model.n_features_in_, "Encoded feature count does not match model."
    MODEL_ERROR = None
except Exception as e:
    model = encoder = encoded_cols = input_cols = categorical_cols = None
    MODEL_ERROR = str(e)

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

@app.get("/api/health")
def health():
    return jsonify(status="online" if MODEL_ERROR is None else "offline",
                   error=MODEL_ERROR,
                   input_features=len(input_cols) if input_cols else 0,
                   encoded_features=len(encoded_cols) if encoded_cols else 0), (200 if MODEL_ERROR is None else 503)

@app.post("/api/analyze")
def analyze():
    if MODEL_ERROR:
        return jsonify(error=MODEL_ERROR), 503
    if "file" not in request.files:
        return jsonify(error="Choose a CSV file."), 400
    try:
        raw = pd.read_csv(io.BytesIO(request.files["file"].read()))
        if raw.empty: return jsonify(error="The CSV has no rows."), 400
        if len(raw) > 100000: return jsonify(error="Maximum 100,000 rows per upload."), 400
        x = raw.drop(columns=["connection_type"], errors="ignore")
        missing = [c for c in input_cols if c not in x.columns]
        if missing: return jsonify(error="Missing required columns: " + ", ".join(missing[:20])), 400
        x = x[input_cols].copy()
        if x.isnull().any().any():
            return jsonify(error="Missing values found in: " + ", ".join(x.columns[x.isnull().any()].tolist()[:15])), 400
        x = pd.get_dummies(x, columns=categorical_cols, dtype=int).reindex(columns=encoded_cols, fill_value=0)
        pred = model.predict(x)
        labels = encoder.inverse_transform(pred)
        out = raw.copy()
        out["Predicted_Result"] = labels
        conf = None
        if hasattr(model, "predict_proba"):
            conf = (model.predict_proba(x).max(axis=1) * 100).round(2)
            out["Model_Confidence_Percent"] = conf
        normal = sum("normal" in str(v).lower() for v in labels)
        attacks = len(labels) - normal
        preview = out.head(250).astype(object).where(pd.notna(out.head(250)), None).to_dict("records")
        return jsonify(filename=request.files["file"].filename, total=len(out), normal=int(normal),
                       attacks=int(attacks), attack_rate=round(attacks/len(out)*100, 2),
                       confidence_average=round(float(conf.mean()), 2) if conf is not None else None,
                       preview=preview, columns=list(out.columns), csv=out.to_csv(index=False))
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
