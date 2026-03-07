
# Student Performance Predictor

An **interactive machine learning project** that predicts a student’s final exam score based on study habits, sleep, attendance, previous performance, and additional factors such as extracurricular activities, class participation, and stress levels.  
Built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**, this project demonstrates **data analysis, predictive modeling, and web app deployment**.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Project Structure](#project-structure)  
5. [Setup & Installation](#setup--installation)  
6. [Usage](#usage)  
7. [Sample Output](#sample-output)  
8. [Future Improvements](#future-improvements)  
9. [Author](#author)  

---

## Project Overview

The **Student Performance Predictor** now predicts a student’s final score using **seven input features**:

- Hours of study per day  
- Hours of sleep per day  
- Attendance percentage  
- Previous academic scores  
- Extracurricular activity hours per week  
- Class participation score (1–5)  
- Stress level (1–10)  

The model has been upgraded to **Random Forest** (with optional XGBoost) for higher accuracy.  
The project includes an **interactive Streamlit web app** to input these features and get real-time predictions.

---

## Features

- Predict final exam scores using **advanced machine learning**  
- Interactive **Streamlit web app** for real-time input  
- Data visualization of relationships between study habits, stress, and scores  
- Clean **project structure** and Git version control  
- Ready to demonstrate for **M1 Data Science / AI applications**

---

## Technologies Used

- **Python** – Programming language  
- **Pandas & NumPy** – Data manipulation and numerical computations  
- **Scikit-learn** – Machine learning models (Random Forest, Linear Regression)  
- **XGBoost** – Optional high-performance model  
- **Matplotlib & Seaborn** – Data visualization  
- **Streamlit** – Interactive web app  
- **Git & GitHub** – Version control and portfolio hosting  

---

## Project Structure

```

student-performance-predictor/
│
├── data/
│   └── students.csv       # Sample dataset including new features
├── src/
│   ├── train_model.py     # Train Random Forest / XGBoost model
│   ├── predict.py         # Make predictions using trained model
│   └── app.py             # Streamlit interactive web app
├── notebooks/             # Optional Jupyter notebooks for analysis
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/Moazzam9/student-performance-predictor
cd student-performance-predictor
````

2. **Create a virtual environment and activate it**

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac:

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

1. **Train the upgraded ML model**

```bash
python src/train_model.py
```

2. **Run prediction script**

```bash
python src/predict.py
```

3. **Launch interactive Streamlit app**

```bash
streamlit run src/app.py
```

Open your browser at `http://localhost:8501`.

---

## Sample Output

* Predicted final score example: **78.5**
* Streamlit app with sliders for all 7 input features
* Visualization showing how study habits, participation, and stress relate to scores

---

## Future Improvements

* Include additional features such as **mental health indicators** or **time management scores**
* Upgrade to **XGBoost** or ensemble models for higher prediction accuracy
* Deploy the Streamlit app online using **Streamlit Cloud** or **Heroku**
* Add **user accounts** to store and compare predictions

---

## Author

**Moazzam Azam** – [GitHub Profile](https://github.com/Moazzam9)
Email: [moazzamkk13@gmail.com](mailto:moazzamkk13@gmail.com)
```




