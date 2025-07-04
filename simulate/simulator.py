import time
import requests
import random

api_url = "http://127.0.0.1:5000/predict"

def generate_synthetic_data():
    if random.random() < 0.15:
        return{

            "vibration_mean": 3.5,     # Very high
            "vibration_std": 1.2,      # Very unstable
            "vibration_max": 4.5,
            "vibration_min": 0.05,
            "humidity_mean": 95,
            "humidity_std": 5,
            "humidity_max": 99,
            "humidity_min": 80,
            "revolution_mean": 50,
            "revolution_std": 8,
            "revolution_max": 70,
            "revolution_min": 30
        }
    else:
        return{
            "vibration_mean": round(random.uniform(0.1, 1.5), 4),
            "vibration_std": round(random.uniform(0.005, 0.5), 4),
            "vibration_max": round(random.uniform(0.3, 2.0), 4),
            "vibration_min": round(random.uniform(0.01, 0.3), 4),
            "humidity_mean": round(random.uniform(30, 90), 2),
            "humidity_std": round(random.uniform(0.1, 5.0), 3),
            "humidity_max": round(random.uniform(35, 100), 2),
            "humidity_min": round(random.uniform(20, 60), 2),
            "revolution_mean": round(random.uniform(5, 40), 2),
            "revolution_std": round(random.uniform(0.1, 5.0), 3),
            "revolution_max": round(random.uniform(10, 60), 2),
            "revolution_min": round(random.uniform(1, 20), 2)
        }

if __name__ == '__main__':
    print("🌐 Starting live data simulator...")
    while True:
        data = generate_synthetic_data()
        try:
            res = requests.post(api_url, json = data)
            if res.status_code == 200:
                print(f"✅ Sent data: Anomaly = {res.json()['is_anomaly']} | Score = {res.json()['anomaly_score']:.4f}")
            else:
                print(f"❌ Error {res.status_code}: {res.json()}")
        except requests.exceptions.RequestException as e:
            print("🚫 Connection Error:", e)

        time.sleep(5)