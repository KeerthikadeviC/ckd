import streamlit as st
import numpy as np
import joblib  # ✅ Replaced pickle with joblib

# Load the trained model using joblib
model = joblib.load('ckd_model.pkl')

# Title
st.title("Chronic Kidney Disease (CKD) Prediction App")

st.markdown("""
This app uses machine learning to predict **Chronic Kidney Disease** (CKD) based on patient input data.
Please enter the following clinical parameters:
""")

# Define all 24 features
feature_names = [
    'age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba',
    'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc',
    'rbcc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'
]

# Create input fields dynamically
input_data = []
for feature in feature_names:
    value = st.number_input(f"{feature}", step=0.1)
    input_data.append(value)

# Predict button
if st.button("Predict"):
    try:
        input_array = np.array([input_data])
        prediction = model.predict(input_array)
        result = "✅ CKD Detected" if prediction[0] == 1 else "🟢 No CKD Detected"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
