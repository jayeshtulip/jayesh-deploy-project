from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save model
os.makedirs("app/model", exist_ok=True)
joblib.dump(clf, "app/model/model.pkl")
print("✅ Model trained and saved to app/model/model.pkl")
