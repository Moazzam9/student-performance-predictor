import pickle
import numpy as np
import pandas as pd


with open("model.pkl", "rb") as f:
    pipeline = pickle.load(f)


input_data = pd.DataFrame(
    [[5, 7, 80, 70, 2, 4, 3]],
    columns=[
        "hours_study", "sleep_hours", "attendance", "previous_score",
        "extracurricular", "class_participation", "stress_level"
    ]
)


prediction = pipeline.predict(input_data)

print(f"🎯 Predicted Final Score: {prediction[0]:.2f}")