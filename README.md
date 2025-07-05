# 🚨 Elevator Anomaly Alert System

A machine learning-based system designed to detect anomalies in elevator sensor data using the Isolation Forest algorithm. This system exposes a Flask API for real-time predictions and logs anomalies into a PostgreSQL database as well as a CSV file.

---

## 🔧 Features

- ✅ Isolation Forest-based anomaly detection
- ✅ Flask REST API for real-time inference
- ✅ PostgreSQL database logging with SQLAlchemy
- ✅ CSV-based fallback logging
- ✅ Docker & deployment ready (optional)
- ✅ Scalable architecture

---

## 🧠 How It Works

1. **Sensor Data Input**: Vibration, humidity, and revolution stats
2. **Inference**: Isolation Forest predicts anomaly score
3. **Logging**: Results logged in:
   - PostgreSQL (`PredictionLog` table)
   - CSV file (`logs/predictions.csv`)
4. **Response**: JSON result indicating anomaly status

---

## 📦 Project Structure
Elevator-Anomaly-Alert-System/
│
├── src/ # Core backend logic
│ ├── api.py # Flask API with /predict route
│ ├── inference.py # Model loading and prediction
│ ├── db.py # DB models and session config
│ └── feature_engineering.py # Optional: Preprocessing (if used)
│
├── model/
│ └── isolation_forest.pkl # Trained model file
│
├── logs/
│ └── predictions.csv # Prediction logs
│
├── simulate/
│ └── simulator.py # Simulated sensor data (optional)
│
├── requirements.txt
├── Procfile # For deployment (e.g., Railway)
├── .env.example # Example environment variables
└── README.md


📌 Tech Stack
| Layer    | Tools                           |
| -------- | ------------------------------- |
| Language | Python 3.9+                     |
| Backend  | Flask                           |
| Model    | Isolation Forest (scikit-learn) |
| Database | PostgreSQL + SQLAlchemy         |
| Hosting  | Railway / EC2 (optional)        |


# 🚀 API Usage

### ▶️ Endpoint

```
POST /predict
```

### 🧾 Request Body (JSON)

```json
{
  "vibration_mean": 0.12,
  "vibration_std": 0.03,
  "vibration_max": 0.22,
  "vibration_min": 0.04,
  "humidity_mean": 35.7,
  "humidity_std": 1.1,
  "humidity_max": 38.2,
  "humidity_min": 33.9,
  "revolution_mean": 120,
  "revolution_std": 4,
  "revolution_max": 125,
  "revolution_min": 115
}
```

### ✅ Response

```json
{
  "anomaly_score": -0.256,
  "is_anomaly": true
}
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Elevator-Anomaly-Alert-System.git
cd Elevator-Anomaly-Alert-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the `src/` folder:

```
DB_HOST=your-rds-endpoint
DB_PORT=5432
DB_NAME=elevator_logs
DB_USER=your-username
DB_PASSWORD=your-password
```

### 5. Run the Application

```bash
cd src
flask run
```

---

## 💻 Running Locally

Once the server is running:

- Send requests via `curl`, Postman, or any HTTP client.
- Output will be printed in terminal, logged in CSV, and inserted into PostgreSQL.

---

## 🌐 Deployment Ready (Optional)

You can deploy this project on:
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- AWS EC2 + RDS

Make sure your `.env` is configured correctly and add a `Procfile` with:

```
web: gunicorn src.api:app
```

---

## 🧪 Sample Curl Request

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d @sample_input.json
```

---

## 📌 Tech Stack

| Layer     | Tools                          |
|-----------|--------------------------------|
| Language  | Python 3.9+                    |
| Backend   | Flask                          |
| Model     | Isolation Forest (scikit-learn)|
| Database  | PostgreSQL + SQLAlchemy        |
| Hosting   | Railway / EC2 (optional)       |

---

## 🧑‍💻 Author

**Yash Patel**

---

