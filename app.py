
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("house_model.pkl")

# App title
st.title("House Price Prediction App")
st.write("Enter house details to predict price")

# User inputs
size = st.number_input("House size (sq ft)", min_value=0)
bedrooms = st.number_input("Number of bedrooms", min_value=0, step=1)
age = st.number_input("House age", min_value=0)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([[size, bedrooms, age]])
    st.success(f"The predicted house price is: ${prediction[0]:,.2f}")
