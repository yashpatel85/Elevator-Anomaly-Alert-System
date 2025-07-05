import pickle
from datetime import datetime
import os
import csv
from .db import SessionLocal, PredictionLog

model = pickle.load(open('model/isolation_forest.pkl', 'rb'))

threshold = -0.15



def infer(features: list, input_dict: dict) -> dict:
    score = model.decision_function([features])[0]
    is_anomaly = score < threshold

    log_data = {
        'timestamp': datetime.now().isoformat(),
        'anomaly_score': score,
        'is_anomaly': is_anomaly,
        **input_dict
    }

    os.makedirs('logs', exist_ok = True)

    log_file = 'logs/predictions.csv'
    write_header = not os.path.exists(log_file)
    with open(log_file, 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = log_data.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(log_data)

        session = SessionLocal()
        try:
            log_entry = PredictionLog(
            anomaly_score=score,
            is_anomaly=is_anomaly,
            vibration_mean=features[0],
            vibration_std=features[1],
            vibration_max=features[2],
            vibration_min=features[3],
            humidity_mean=features[4],
            humidity_std=features[5],
            humidity_max=features[6],
            humidity_min=features[7],
            revolution_mean=features[8],
            revolution_std=features[9],
            revolution_max=features[10],
            revolution_min=features[11],
            )
            session.add(log_entry)
            session.commit()
        finally:
            session.close()


        return{'anomaly_score': float(score), 'is_anomaly': bool(score < threshold)}


