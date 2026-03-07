import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


data = pd.read_csv("data/students.csv")

data.columns = data.columns.str.strip()


X = data[
    [
        "hours_study", "sleep_hours", "attendance", "previous_score",
        "extracurricular", "class_participation", "stress_level"
    ]
]


y = data["final_score"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved with new features!")