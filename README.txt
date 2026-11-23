# 🛡️ SENTINEL — AI-Powered Network Intrusion Detection System

**SENTINEL** is a machine-learning-based Network Intrusion Detection System (NIDS) that analyzes uploaded network traffic CSV files and identifies potentially malicious activity using a trained **Random Forest Classifier**.

The application combines a Flask backend with a responsive HTML, CSS, and JavaScript frontend to provide an interactive interface for network traffic analysis.

> **Note:** SENTINEL analyzes uploaded CSV datasets. It does not capture or monitor live network packets.

---

## ✨ Features

- 🤖 **Machine Learning Detection:** Uses a trained Random Forest model to classify network traffic.
- 📂 **CSV File Upload:** Upload network traffic datasets for analysis.
- 🔍 **Intrusion Detection:** Identifies traffic as Normal or Attack.
- 📊 **Analysis Dashboard:** Displays prediction summaries and traffic statistics.
- 📈 **Confidence Score:** Shows model confidence when probability predictions are available.
- 📥 **Download Results:** Export analyzed results as a CSV file.
- 🌐 **Web-Based Interface:** Simple frontend built using HTML, CSS, and JavaScript.
- ⚡ **Flask Backend:** Handles file processing and model predictions.
- ☁️ **Cloud Deployment:** Can be deployed using Render.

---

## 🏗️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Machine Learning | Scikit-learn |
| Model | Random Forest Classifier |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib |
| Deployment | Render, Gunicorn |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
SENTINEL/
│
├── app.py
├── requirements.txt
│
├── ids_random_forest_model.pkl
├── ids_label_encoder.pkl
├── ids_feature_columns.pkl
├── ids_input_columns.pkl
├── ids_categorical_columns.pkl
│
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

### Machine Learning Model Files

The following five `.pkl` files are required for the application to load the trained model and process input data.

| File | Purpose |
|---|---|
| `ids_random_forest_model.pkl` | Trained Random Forest model |
| `ids_label_encoder.pkl` | Converts predicted labels back to their original classes |
| `ids_feature_columns.pkl` | Stores the encoded feature-column structure |
| `ids_input_columns.pkl` | Stores the required input features |
| `ids_categorical_columns.pkl` | Stores categorical feature names |

**Important:** Keep all five `.pkl` files in the same directory as `app.py`.

---

## ⚙️ Installation and Local Setup

### Prerequisites

- Python 3.12 recommended
- Git
- A web browser

### Step 1: Clone the Repository

```bash
git clone https://github.com/vivek9158/Instruction-Detection-System.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Instruction-Detection-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Verify Model Files

Make sure all five `.pkl` files are present beside `app.py`.

### Step 7: Run the Application

```bash
python app.py
```

### Step 8: Open the Application

Open your browser and visit:

**http://127.0.0.1:5000**

---

## ☁️ Deployment on Render

SENTINEL can be deployed using [Render](https://render.com/).

### Deployment Configuration

| Setting | Value |
|---|---|
| Runtime | Python |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

### Deployment Steps

1. Push the project to a GitHub repository.
2. Log in to Render.
3. Create a new **Web Service**.
4. Connect your GitHub repository.
5. Select the `main` branch.
6. Configure the build and start commands.
7. Click **Deploy Web Service**.
8. Open the generated public URL.

---

## 📤 CSV Upload Limitations

The current backend enforces the following upload restrictions:

| Parameter | Maximum Limit |
|---|---:|
| CSV file size | 100 MB |
| Number of rows | 100,000 |

**Note:** Both restrictions must be satisfied for a CSV file to be processed successfully.

---

## 🔄 Application Workflow

```text
        CSV File Upload
               │
               ▼
       Flask Backend
               │
               ▼
       Input Validation
               │
               ▼
     Data Preprocessing
               │
               ▼
    Random Forest Model
               │
               ▼
       Classification
          /       \
         /         \
      Normal      Attack
         \         /
          \       /
               ▼
       Results Dashboard
               │
               ▼
        Download CSV
```

---

## 🎯 Project Objective

The primary objective of SENTINEL is to demonstrate how machine learning can support network intrusion detection by analyzing network traffic data and identifying suspicious activity.

The system provides an accessible web interface for uploading datasets, running predictions, viewing analysis results, and exporting classified data.

---

## 🚀 Future Enhancements

- Real-time network traffic monitoring.
- Live packet capture and analysis.
- Advanced anomaly detection techniques.
- Network activity visualization.
- Alert and notification system.
- Integration with additional machine learning models.

---

## 👨‍💻 Author

**Vivek Badgujar**

Electronics and Telecommunication Engineering  
MIT Academy of Engineering, Alandi, Pune

GitHub: [@vivek9158](https://github.com/vivek9158)

---

## 📜 License

This project is developed for educational and academic purposes.

---

<p align="center">
  <b>🛡️ SENTINEL — Smarter Network Traffic Analysis Through Machine Learning.</b>
</p>
