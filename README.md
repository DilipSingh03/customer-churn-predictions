# 📊 Telco Customer Churn Prediction

## Overview

This project is an end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn (leave the service) based on customer demographics, account information, subscribed services, and billing details. The model is deployed using **Streamlit**, allowing users to make real-time predictions through an interactive web interface.

---

## Features

* End-to-end Machine Learning pipeline
* Data preprocessing and feature engineering
* Exploratory Data Analysis (EDA)
* Handling categorical and numerical features
* Feature scaling using StandardScaler
* Customer churn prediction using a trained classification model
* Interactive Streamlit web application
* Real-time prediction with churn probability

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Matplotlib
* Seaborn

---

## Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── customer_churn_model.pkl
├── standard_scaler.pkl
├── requirements.txt
├── README.md
├── Customer_Churn_Prediction_using_ML.ipynb
│── WA_Fn-UseC_-Telco-Customer-Churn

```

---

## Dataset

The project uses the **Telco Customer Churn** dataset, which contains customer demographics, subscription details, service usage, billing information, and churn status.

### Input Features

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

### Target Variable

* **Churn**

  * 0 → Customer Stays
  * 1 → Customer Churns

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Encoding
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Serialization
10. Streamlit Deployment

---

## Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

---

## Installation

Move into the project directory:

```bash
cd Customer-Churn-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## How It Works

1. Enter customer details using the Streamlit interface.
2. Numerical features are scaled using the saved `StandardScaler`.
3. The trained Machine Learning model predicts whether the customer is likely to churn.
4. The application displays:

   * Churn Prediction
   * Churn Probability
   * Stay Probability

---

## Future Improvements

* Hyperparameter tuning
* Cross-validation
* Explainable AI using SHAP
* REST API with FastAPI
* Docker containerization
* Cloud deployment (Streamlit Community Cloud, Render, or Azure)
* Automated model retraining

---

## Author

**Dilip Singh Shaktawat**

* GitHub: https://github.com/DilipSingh03
* LinkedIn: https://www.linkedin.com/in/dilip-singh-77581b409

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and contribute to this project.

