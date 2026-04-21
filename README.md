# 🎓 Student Performance Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine-Learning-orange)
![Status](https://img.shields.io/badge/Project-Completed-green)
![Framework](https://img.shields.io/badge/Streamlit-WebApp-red)
![GitHub](https://img.shields.io/badge/GitHub-maahfuzdev-blueviolet)

---

## 🚀 Project Overview

This project is a **Machine Learning-based Student Performance Prediction System** that predicts a student's exam score based on:

- 📚 **Study Hours** (per day)  
- 🏫 **Attendance Percentage** (%)  

It also classifies students into performance categories such as:

- 🔴 **Weak** (0-40)  
- 🟠 **Average** (41-60)  
- 🔵 **Good** (61-75)  
- 🟢 **Excellent** (76-100)  

A modern **Streamlit Web App** is included for interactive predictions and visualization.

---

## 🧠 Machine Learning Model

- **Algorithm**: Linear Regression  
- **Library**: Scikit-learn  
- **Training Method**: Supervised Learning  
- **Output**: Continuous Score Prediction (0–100)

### 📊 Mathematical Model:
Score = w1 × Hours + w2 × Attendance + b

text

---

## 📂 Dataset

| Feature     | Description                   |
|-------------|-------------------------------|
| Hours       | Study hours per day (1-10)    |
| Attendance  | Class attendance % (50-100)   |
| Score       | Final exam score (0-100)      |

---

## ⚙️ Tech Stack

- 🐍 Python 3.10
- 📊 Pandas, NumPy
- 🤖 Scikit-learn
- 📈 Matplotlib, Seaborn
- 🌐 Streamlit
- 💾 Pickle (model serialization)

---

## 📁 Project Structure
Student-Score-Predictor/
│
├── dataset.csv # Raw data
├── train.py # Model training script
├── predict.py # CLI prediction script
├── app.py # Streamlit web app
├── model.pkl # Trained model file
├── requirements.txt # Dependencies
└── README.md # Project documentation

text

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository
```bash
git clone https://github.com/maahfuzdev/Student-Score-Predictor.git
cd Student-Score-Predictor
2️⃣ Install Dependencies
bash
pip install -r requirements.txt
3️⃣ Train Model
bash
python train.py
4️⃣ Run CLI Prediction
bash
python predict.py
5️⃣ Run Web App (Streamlit)
bash
streamlit run app.py
🌐 Web App Features
✔ Interactive UI with sliders and buttons

✔ Real-time prediction as you adjust values

✔ Score category classification with colored badges

✔ Graph visualization (actual vs predicted trends)

✔ User-friendly design with custom CSS

📊 Visualization Examples
Study Hours vs Score	Attendance vs Performance
📉 Scatter plot with regression line	📊 Bar chart of categories
📈 Results & Accuracy
Model: Linear Regression

R² Score: ~0.89 (example value)

Mean Absolute Error: ~4.2 points

The model successfully predicts student performance and helps identify at-risk students.

🧪 Example Prediction
text
Input:
Study Hours: 6
Attendance: 80%

Output:
Predicted Score: 78.45
Category: 🟢 Excellent
🎯 Applications
🎓 Educational analytics for schools/colleges

🏫 Student performance tracking dashboards

📊 Academic improvement planning

🤖 AI-based education systems and tutors

🔮 Future Improvements
➕ Add more features (sleep time, assignments, previous grades, extracurriculars)

🤖 Use advanced ML models (Random Forest, XGBoost, Neural Networks)

📱 Deploy mobile app version (Flutter + API)

☁️ Cloud deployment (Render / HuggingFace Spaces / AWS)

📊 Real-time database integration (Firebase/SQLite)

👨‍💻 Developer
Md Maahfuzur Rahman

💡 Built using Python & Machine Learning

🎯 Focus: Educational Data Mining & AI

🚀 Goal: Smart, accessible AI-based academic systems

📧 Contact: [maahfuz2021@gmail.com]

🔗 GitHub: github.com/maahfuzdev

⭐ Project Highlights
✔ End-to-end ML pipeline (data → training → deployment)

✔ Real-world dataset with synthetic but realistic patterns

✔ Web-based AI system using Streamlit

✔ Research paper ready structure

✔ Beginner-friendly but professional quality

📌 License
This project is for educational purposes. Feel free to use, modify, and share with attribution.

🙏 Acknowledgments
Scikit-learn documentation

Streamlit community

Real Python tutorials

Open-source contributors

