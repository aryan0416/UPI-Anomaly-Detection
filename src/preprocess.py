import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def preprocess_features(df):
    categorical_features = pd.get_dummies(df[['merchant_category', 'day_of_week']], drop_first=True)
    features = pd.concat([df[['amount (INR)', 'hour_of_day']], categorical_features], axis=1)
    return features
