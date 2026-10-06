import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import numpy as np

df = pd.read_csv('upi_data.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.dayofweek

categorical_features = pd.get_dummies(df['MerchantCategory'], drop_first=True)
features = pd.concat([df[['Amount_INR', 'Hour', 'DayOfWeek']], categorical_features], axis=1)

model = IsolationForest(contamination=0.05, random_state=42)
df['Anomaly'] = model.fit_predict(features)
df['Anomaly'] = df['Anomaly'].map({1: 0, -1: 1})

print("Anomaly counts:\n", df['Anomaly'].value_counts())

y_true = np.zeros(len(df))
print(classification_report(y_true, df['Anomaly'], zero_division=0))
