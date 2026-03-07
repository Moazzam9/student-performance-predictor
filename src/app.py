import streamlit as st
import pickle
import numpy as np


with open("model.pkl","rb") as f:
    model = pickle.load(f)

st.title("Student Performance Predictor")


hours_study = st.number_input("Hours of Study per Day", min_value=0, max_value=24, value=5)
sleep_hours = st.number_input("Hours of Sleep per Day", min_value=0, max_value=24, value=7)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=80)
previous_score = st.number_input("Previous Score", min_value=0, max_value=100, value=70)

if st.button("Predict Score"):
    input_data = np.array([[hours_study, sleep_hours, attendance, previous_score]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Final Score: {prediction[0]:.2f}")