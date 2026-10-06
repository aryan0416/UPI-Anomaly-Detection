# UPI Anomaly Detection

![UPI Banner](banner.jpg)

## Business Problem
The exponential growth of Unified Payments Interface (UPI) transactions has revolutionized digital payments in India. However, this scale also attracts fraudulent activities. Detecting anomalous transactions in real-time is essential for preventing financial loss and maintaining user trust. This project builds a machine learning pipeline to detect unusual patterns in UPI transaction data, mitigating financial risks associated with digital payment fraud.

## Tech Stack
* **Python**: Core programming language.
* **Pandas**: For data preprocessing and feature engineering.
* **Scikit-Learn**: For implementing the Isolation Forest algorithm and evaluation metrics.
* **NumPy**: For numerical array operations.

## Methodology
1. **Data Ingestion**: The script reads the transaction records.
2. **Feature Engineering**: Time-based features (Hour, Day of Week) are extracted from timestamps. Merchant categories are one-hot encoded to provide categorical context to the model.
3. **Model Training**: An Isolation Forest algorithm, which is highly effective for unsupervised anomaly detection, is trained on the engineered features. We assume a baseline contamination rate of 5%.
4. **Prediction and Evaluation**: The model flags anomalies (-1) and normal transactions (1), which are then mapped to standard binary classes (1 for anomaly, 0 for normal). A classification report is generated to evaluate the detection footprint.

## Business Impact
Detecting fraud before funds are irrecoverably transferred provides immense value:
* Drastic reduction in financial losses for both the platform and the consumers.
* Enhanced regulatory compliance and risk management.
* Increased user confidence in the digital payment ecosystem, driving further adoption.

## Setup Instructions
**Prerequisites:**
You must provide the dataset `upi_data.csv` in the root of this directory. The CSV must contain the following columns: `TransactionID`, `Timestamp`, `MerchantCategory`, and `Amount_INR`.

**Execution:**
Run the analysis script using the following command:
```bash
python main.py
```
This will output the anomaly counts and a classification report based on the Isolation Forest predictions.
