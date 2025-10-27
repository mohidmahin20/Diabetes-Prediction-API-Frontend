import streamlit as st
import requests

st.title("🩺 Diabetes Prediction App")
st.markdown("Enter patient information to predict diabetes status.")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1, step=1)

# On button click
if st.button("Predict"):
    payload = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    BACKEND_URL = "https://diabetes-prediction-api-r4pb.onrender.com/predict"


    try:
        response = requests.post(BACKEND_URL, json=payload)
        result = response.json()

        st.success(f"Prediction: {result['result']}")
        st.info(f"Confidence: {result['confidence'] * 100:.2f}%")
    except:
        st.error("Something went wrong. Please check your API or input values.")
