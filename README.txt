SENTINEL HTML/CSS/JS + Flask application

Copy the five existing .pkl files beside app.py:
ids_random_forest_model.pkl
ids_label_encoder.pkl
ids_feature_columns.pkl
ids_input_columns.pkl
ids_categorical_columns.pkl

Windows local run (Python 3.12 recommended):
  python -m venv venv
  .\venv\Scripts\activate
  python -m pip install -r requirements.txt
  python app.py
Open http://127.0.0.1:5000

Render:
Build command: pip install -r requirements.txt
Start command: gunicorn app:app

This application analyzes uploaded CSV files; it does not capture live network packets.
