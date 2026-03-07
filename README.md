
Student Performance Predictor

An **interactive machine learning project** that predicts a student’s final exam score based on study habits, sleep, attendance, and previous performance.  
Built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**, this project demonstrates **data analysis, predictive modeling, and web app deployment**.



## Project Overview

The **Student Performance Predictor** uses a **Linear Regression model** to predict a student’s final score based on four key factors:  

- Hours of study per day  
- Hours of sleep per day  
- Attendance percentage  
- Previous academic scores  

The project also includes an **interactive Streamlit web app** to input these features and receive predictions in real-time.

---

## Features

- Predict student scores using **machine learning**  
- Interactive **web interface** with Streamlit  
- Data visualization of study habits vs final score  
- Clean **project structure** and version control using Git  
- Ready to demonstrate for **M1 Data Science / AI applications**

---

## Technologies Used

- **Python** – Programming language  
- **Pandas & NumPy** – Data manipulation and numerical computations  
- **Scikit-learn** – Machine learning models  
- **Matplotlib & Seaborn** – Data visualization  
- **Streamlit** – Interactive web application  
- **Git & GitHub** – Version control and portfolio hosting  

---

## Project Structure

```

student-performance-predictor/
│
├── data/
│   └── students.csv       # Sample dataset
├── src/
│   ├── train_model.py     # Script to train the ML model
│   ├── predict.py         # Script to make predictions
│   └── app.py             # Streamlit interactive web app
├── notebooks/             # Optional Jupyter notebooks for analysis
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/student-performance-predictor.git
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

1. **Train the ML model**

```bash
python src/train_model.py
```

2. **Run prediction script**

```bash
python src/predict.py
```

3. **Launch Streamlit interactive app**

```bash
streamlit run src/app.py
```

Open your browser at: `http://localhost:8501`

---

## Sample Output

* Predicted final score example: **78.5**
* Interactive web app with input sliders and real-time prediction
* Graph showing study hours vs final score

---

## Future Improvements

* Include additional features: extracurricular activities, class participation, stress levels
* Upgrade ML model to **Random Forest** or **XGBoost** for higher accuracy
* Deploy the Streamlit app online using **Streamlit Cloud** or **Heroku**
* Add **user authentication** and **data storage** for a multi-user platform

---

## Author

**Moazzam Azam** – [GitHub Profile](https://github.com/Moazzam9/student-performance-predictor)
Email: [moazzamkk13@gmail.com](mailto:moazzamkk13@gmail.com)

