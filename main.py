from src.preprocess import load_data, preprocess_features
from src.model import train_and_predict, evaluate_predictions

def main():
    df = load_data('data/upi_data.csv')
    features = preprocess_features(df)
    df = train_and_predict(features, df)
    evaluate_predictions(df)

if __name__ == "__main__":
    main()
