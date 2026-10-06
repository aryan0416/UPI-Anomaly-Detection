# UPI Anomaly Detection

![UPI Banner](banner.jpg)

## Business Problem
The exponential growth of Unified Payments Interface (UPI) transactions has revolutionized digital payments in India. However, this scale also attracts fraudulent activities. Detecting anomalous transactions in real-time is essential for preventing financial loss and maintaining user trust. This project builds a machine learning pipeline to detect unusual patterns in UPI transaction data, mitigating financial risks associated with digital payment fraud.

## Tech Stack
* **Python**: Core programming language.
* **Pandas**: For data preprocessing and feature engineering.
* **Scikit-Learn**: For implementing the Isolation Forest algorithm and evaluation metrics.

## Methodology
1. **Data Ingestion**: The script reads the transaction records from the `data/` directory.
2. **Feature Engineering**: Time-based features and merchant categories are processed. Categorical data is transformed using one-hot encoding.
3. **Model Training**: An Isolation Forest algorithm, which is highly effective for unsupervised anomaly detection, is trained on the engineered features assuming a contamination rate of 5%.
4. **Prediction and Evaluation**: The model flags anomalies and compares them against true fraud labels to generate a classification report.

## Project Structure
* `data/`: Contains the raw dataset.
* `src/`: Modularized python scripts (`preprocess.py`, `model.py`).
* `main.py`: The entry point script to run the pipeline.
* `requirements.txt`: Python package dependencies.

## Results
The unsupervised Isolation Forest model was executed on 250,000 transactions. The pipeline produced the following insights:
* **Total Anomalies Detected:** 12,499
* **Overall Accuracy:** 0.95

## Setup Instructions
**Prerequisites:**
Place the dataset inside the `data/` directory and rename it to `upi_data.csv`.

Install dependencies:
```bash
pip install -r requirements.txt
```

**Execution:**
Run the machine learning pipeline using the following command:
```bash
python main.py
```
