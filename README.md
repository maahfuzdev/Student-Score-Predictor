# 🎓 Student Performance Prediction using Machine Learning

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-maahfuzdev-blueviolet?style=for-the-badge\&logo=github)

</p>

---

## 🚀 Live Demo

👉 **Click to Open Web App**

🌐 **Live App:**
https://student-score-predictor-hrykgxexqb5k96txlzmrwb.streamlit.app/

---

## 📌 Project Overview

**Student Performance Prediction System** is a Machine Learning project that predicts student exam scores based on academic behavior.

The system analyzes:

* 📚 Study Hours (per day)
* 🏫 Attendance Percentage

and intelligently predicts final exam performance.

It also classifies students into performance levels:

| Score Range | Category     |
| ----------- | ------------ |
| 0 – 40      | 🔴 Weak      |
| 41 – 60     | 🟠 Average   |
| 61 – 75     | 🔵 Good      |
| 76 – 100    | 🟢 Excellent |

A modern **Streamlit Web Application** allows real-time prediction and visualization.

---

## 🧠 Machine Learning Model

**Algorithm:** Linear Regression
**Learning Type:** Supervised Learning
**Library:** Scikit-learn

### Mathematical Model

Score = w₁ × Study Hours + w₂ × Attendance + b

The model learns relationships between study behavior and academic performance.

---

## 📊 Dataset Information

| Feature    | Description                     |
| ---------- | ------------------------------- |
| Hours      | Study hours per day (1–10)      |
| Attendance | Attendance percentage (50–100%) |
| Score      | Final exam score (0–100)        |

---

## ⚙️ Tech Stack

* 🐍 Python 3.10
* 🤖 Scikit-learn
* 📊 Pandas & NumPy
* 📈 Matplotlib & Seaborn
* 🌐 Streamlit
* 💾 Pickle (Model Serialization)

---

## 📁 Project Structure

```
Student-Score-Predictor/
│
├── dataset.csv
├── train.py
├── predict.py
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

```
git clone https://github.com/maahfuzdev/Student-Score-Predictor.git
cd Student-Score-Predictor
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train Model

```
python train.py
```

### 4️⃣ CLI Prediction

```
python predict.py
```

### 5️⃣ Run Streamlit Web App

```
streamlit run app.py
```

---

## 🌐 Web Application Features

✅ Interactive sliders
✅ Real-time prediction
✅ Performance category classification
✅ Data visualization graphs
✅ Clean modern UI
✅ Beginner-friendly AI system

---

## 📈 Model Performance

| Metric              | Value             |
| ------------------- | ----------------- |
| Model               | Linear Regression |
| R² Score            | ~0.89             |
| Mean Absolute Error | ~4.2              |

The model effectively identifies student performance trends and risk levels.

---

## 🧪 Example Prediction

**Input**

```
Study Hours: 6
Attendance: 80%
```

**Output**

```
Predicted Score: 78.45
Category: Excellent 🟢
```

---

## 🎯 Real-World Applications

* 🎓 Educational Analytics Systems
* 🏫 Student Monitoring Dashboards
* 📊 Academic Improvement Planning
* 🤖 AI-based Learning Platforms
* 📚 Smart Education Research Projects

---

## 🔮 Future Improvements

* ➕ Add more student features (sleep, assignments, GPA)
* 🤖 Advanced ML models (Random Forest, XGBoost)
* 📱 Mobile App (Flutter + API)
* ☁️ Cloud Deployment Expansion
* 📊 Real-time Database Integration

---

## 👨‍💻 Developer

**Md Maahfuzur Rahman**

💡 Machine Learning & AI Enthusiast
🎯 Focus: Educational Data Mining & Smart Systems

📧 Email: [maahfuz2021@gmail.com](mailto:maahfuz2021@gmail.com)
🔗 GitHub: https://github.com/maahfuzdev

---

## ⭐ Project Highlights

✔ End-to-End Machine Learning Pipeline
✔ Model Training → Prediction → Deployment
✔ Streamlit AI Web Application
✔ Portfolio & Research Ready Project
✔ Clean Professional Structure

---

## 📜 License

This project is created for **educational and learning purposes**.
You are free to use, modify, and share with attribution.

---

## 🙏 Acknowledgments

* Scikit-learn Documentation
* Streamlit Community
* Open-Source Contributors
* Python ML Ecosystem ❤️

---

<p align="center">
⭐ If you like this project, don't forget to star the repository!
</p>
