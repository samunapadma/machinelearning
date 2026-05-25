import streamlit as st
import pickle
import numpy as np

# Model load பண்ணு
with open("salary_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💰 Salary Predictor")
st.write("Years of Experience கொடுத்து Salary பாருங்க!")

# Input
years = st.slider("Years of Experience", 1, 15, 5)

# Predict
if st.button("Predict Salary"):
    result = model.predict([[years]])
    st.success(f"💵 Predicted Salary: ₹{result[0]:,.0f}")
