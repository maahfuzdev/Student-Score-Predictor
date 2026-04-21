import pickle
import numpy as np

print("=== Student Score Predictor ===")

try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    print("Model not found! Run train.py first.")
    exit()

try:
    hours = float(input("Study Hours: "))
    attendance = float(input("Attendance (%): "))

    # prediction
    result = model.predict([[hours, attendance]])
    score = result[0]

    # 🔥 FIX: bound between 0 and 100
    score = max(0, min(100, score))

    print(f"\nPredicted Score: {score:.2f}")

    # Category system
    if score < 40:
        print("Category: Weak")
    elif score < 60:
        print("Category: Average")
    elif score < 80:
        print("Category: Good")
    else:
        print("Category: Excellent")

except:
    print("Invalid input!")