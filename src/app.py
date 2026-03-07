import streamlit as st
import pickle
import numpy as np

with open("model.pkl","rb") as f:
    model = pickle.load(f)

st.title("Student Performance Predictor with Extended Features")

hours_study = st.number_input("Hours of Study per Day", 0, 24, 5)
sleep_hours = st.number_input("Hours of Sleep per Day", 0, 24, 7)
attendance = st.number_input("Attendance (%)", 0, 100, 80)
previous_score = st.number_input("Previous Score", 0, 100, 70)
extracurricular = st.number_input("Extracurricular Hours per Week", 0, 20, 2)
class_participation = st.number_input("Class Participation Score (1-5)", 1, 5, 4)
stress_level = st.number_input("Stress Level (1-10)", 1, 10, 3)

if st.button("Predict Score"):
    input_data = np.array([[hours_study, sleep_hours, attendance, previous_score, extracurricular, class_participation, stress_level]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Final Score: {prediction[0]:.2f}")