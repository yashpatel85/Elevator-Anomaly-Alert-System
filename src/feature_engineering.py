import pandas as pd

def extract_features(df2, window_size = 120):
    feats = []
    for start in range(0, len(df2), window_size):
        window = df2.iloc[start:start + window_size]
        if len(window) < window_size:
            break
        feats.append({f"{col}_{func}": getattr(window[col], func)()
                     for col in ['vibration', 'humidity', 'revolutions']
                     for func in ['mean', 'std', 'max', 'min']})
    return pd.DataFrame(feats)

df2 = pd.read_csv('D:\ML_Practice_Projects\Advanced\Elevator Anomaly Alert System\data\predictive-maintenance-dataset.csv')


import csv

features_df = extract_features(df2)

features_df.to_csv('data/features.csv', index = False)