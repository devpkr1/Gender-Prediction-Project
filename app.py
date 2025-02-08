import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('logistic regression.pkl')

# Streamlit app title
st.title("Gender Prediction App")

# User input
name = st.text_input("Enter a Name:")
name = name.lower()

if st.button("Predict Gender"):
    # Preprocess the name and make prediction
    prediction = model.predict([name])  # Adjust based on preprocessing
    gender = 'Male' if prediction[0] == 1 else 'Female'
    st.write(f"The predicted gender is: **{gender}**")
