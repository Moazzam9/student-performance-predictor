

# 📚 Student Performance Predictor with Extended Features

Predict a student’s final exam score based on multiple factors like study habits, sleep, attendance, previous performance, extracurricular activities, class participation, and stress levels.

---

## 🚀 Features

* Predict final exam scores using a **Random Forest Regression pipeline**.
* Includes **7 input features**:

  * Hours of Study per Day
  * Sleep Hours per Day
  * Attendance (%)
  * Previous Exam Score
  * Extracurricular Hours per Week
  * Class Participation Score (1–5)
  * Stress Level (1–10)
* **Streamlit Web App** for interactive predictions.
* **Standalone Python script** for batch or one-off predictions.
* **Visualization scripts**: scatter plots and pairplots to analyze features vs. final score.
* **Preprocessing included** (scaling) for consistent predictions.
* Works with **robust relative paths**—no file-not-found errors.

---

## 📁 Project Structure

```
student-performance-predictor/
│
├── data/
│   └── students.csv          # Dataset including extended features
├── src/
│   ├── train_model.py        # Train Random Forest model with pipeline
│   ├── predict.py            # Make predictions using trained model
│   └── app.py                # Streamlit interactive web app
├── notebooks/                # Optional Jupyter notebooks for analysis
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚡ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd student-performance-predictor
```

### 2. Create a Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
cd src
python train_model.py
```

* Outputs evaluation metrics: **MAE, RMSE, R²**.
* Saves trained pipeline to `src/model.pkl`.

### 5. Run Streamlit App

```bash
streamlit run app.py
```

* Fill in the input fields.
* Click **Predict Score** to get a prediction.

### 6. Make Standalone Predictions

```bash
python predict.py
```

* Uses `model.pkl` to output predictions for sample inputs.

### 7. Visualize Data

```bash
python visualize.py
```

* Displays scatter plots and pairplots for feature analysis.

---

## 📊 Evaluation Metrics

| Metric | Value |
| ------ | ----- |
| MAE    | 1.34  |
| RMSE   | 2.01  |
| R²     | 0.90  |

✅ The model performs well with the expanded dataset.

---

## 💡 Next Improvements

* Add more **student data** to further improve accuracy.
* Try other regressors: **XGBoost**, **Gradient Boosting**, or **Linear Regression**.
* Add **cross-validation** for more robust evaluation.
* Enhance **Streamlit app UI**: sliders, charts, downloadable reports.
* Add **unit tests** for model predictions and scripts.

---

## 🔗 Useful Links

* **Streamlit App**: `src/app.py`
* **Prediction Script**: `src/predict.py`
* **Training Script**: `src/train_model.py`
* **Visualization**: `src/visualize.py`



## 📝 License

This project is open-source and available under the MIT License.

