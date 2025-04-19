from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# ✅ Load the model using the correct relative path
model = joblib.load("model/model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "jayesh- CI CD WORKING"}

@app.post("/predict")
def predict_species(data: IrisInput):
    x = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(x)
    return {"predicted_class": int(prediction[0])}
