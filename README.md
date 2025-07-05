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

