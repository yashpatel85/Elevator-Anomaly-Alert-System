from sklearn.ensemble import IsolationForest
import pickle, pandas as pd

features_dataframe = pd.read_csv('data/features.csv')
model = IsolationForest(contamination = 0.01, random_state = 42)
model.fit(features_dataframe)
pickle.dump(model, open('model/isolation_forest.pkl', 'wb'))