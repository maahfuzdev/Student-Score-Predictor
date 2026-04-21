import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Student AI Predictor", page_icon="🎓", layout="centered")

st.title("🎓 Smart Student Performance Predictor (AI)")
st.write("Predict student exam score using Machine Learning")

# Sidebar
st.sidebar.header("📊 Input Features")

hours = st.sidebar.slider("Study Hours", 0.0, 24.0, 5.0)
attendance = st.sidebar.slider("Attendance (%)", 0.0, 100.0, 75.0)

# Predict button
if st.button("🚀 Predict Score"):

    result = model.predict([[hours, attendance]])
    score = result[0]

    # limit 0-100
    score = max(0, min(100, score))

    st.subheader("📌 Prediction Result")
    st.success(f"Predicted Score: {score:.2f}")

    # Category
    if score < 40:
        st.error("Category: Weak")
    elif score < 60:
        st.warning("Category: Average")
    elif score < 80:
        st.info("Category: Good")
    else:
        st.success("Category: Excellent")

# Dataset Graph Section
st.subheader("📊 Data Visualization")

data = pd.read_csv("dataset.csv")

fig, ax = plt.subplots()
ax.scatter(data["Hours"], data["Score"], color="blue")
ax.set_xlabel("Study Hours")
ax.set_ylabel("Score")
ax.set_title("Hours vs Score")

st.pyplot(fig)