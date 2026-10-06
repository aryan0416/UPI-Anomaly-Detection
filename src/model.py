from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

def train_and_predict(features, df):
    model = IsolationForest(contamination=0.05, random_state=42)
    predictions = model.fit_predict(features)
    df['Anomaly_Pred'] = predictions
    df['Anomaly_Pred'] = df['Anomaly_Pred'].map({1: 0, -1: 1})
    return df

def evaluate_predictions(df):
    print("Anomaly predictions counts:\n", df['Anomaly_Pred'].value_counts())
    if 'fraud_flag' in df.columns:
        print("\nClassification Report against Actual Fraud Flag:")
        print(classification_report(df['fraud_flag'], df['Anomaly_Pred'], zero_division=0))
