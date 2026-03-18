import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
import numpy as np

data = pd.read_csv("data/students.csv")
data.columns = data.columns.str.strip()


X = data[
    [
        "hours_study", "sleep_hours", "attendance", "previous_score",
        "extracurricular", "class_participation", "stress_level"
    ]
]
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")


with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Pipeline trained and saved successfully!")