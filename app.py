import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("customer_churn_model.pkl", "rb"))
scaler = pickle.load(open("standard_scaler.pkl", "rb"))

st.title("📊 Telco Customer Churn Prediction")

st.write("Fill in the customer details below.")

# ---------------- INPUT ----------------

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (Months)", 1, 72, 12)

phone = st.selectbox("Phone Service", ["No", "Yes"])
multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])

tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input("Monthly Charges", value=50.0)
total = st.number_input("Total Charges", value=1000.0)

# ---------------- PREDICTION ----------------

if st.button("Predict"):

    # Convert text into numbers
    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone == "Yes" else 0,
        "MultipleLines": {"No":0,"Yes":1,"No phone service":2}[multiple],
        "InternetService": {"DSL":0,"Fiber optic":1,"No":2}[internet],
        "OnlineSecurity": {"No":0,"Yes":1,"No internet service":2}[security],
        "OnlineBackup": {"No":0,"Yes":1,"No internet service":2}[backup],
        "DeviceProtection": {"No":0,"Yes":1,"No internet service":2}[protection],
        "TechSupport": {"No":0,"Yes":1,"No internet service":2}[support],
        "StreamingTV": {"No":0,"Yes":1,"No internet service":2}[tv],
        "StreamingMovies": {"No":0,"Yes":1,"No internet service":2}[movies],
        "Contract": {"Month-to-month":0,"One year":1,"Two year":2}[contract],
        "PaperlessBilling": 1 if paperless == "Yes" else 0,
        "PaymentMethod": {
            "Electronic check":0,
            "Mailed check":1,
            "Bank transfer (automatic)":2,
            "Credit card (automatic)":3
        }[payment],
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    # Create DataFrame
    df = pd.DataFrame([data])

    # Scale numerical columns
    df[["tenure", "MonthlyCharges", "TotalCharges"]] = scaler.transform(
    df[["tenure", "MonthlyCharges", "TotalCharges"]]
)

    # Prediction
    result = model.predict(df)[0]
    probability = model.predict_proba(df)[0]

    if result == 1:
        st.error("⚠ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    st.write(f"Churn Probability : {probability[1]:.2f}")
    st.write(f"No Churn Probability : {probability[0]:.2f}")