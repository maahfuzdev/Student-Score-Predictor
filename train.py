import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

print("Loading dataset...")

data = pd.read_csv("dataset.csv")

X = data[["Hours", "Attendance"]]
y = data["Score"]

# 🔥 Train/Test split (REAL ML practice)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = LinearRegression()
model.fit(X_train, y_train)

# prediction check
y_pred = model.predict(X_test)

accuracy = r2_score(y_test, y_pred)

print(f"Model Accuracy (R² Score): {accuracy:.2f}")

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")