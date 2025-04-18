from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

model_path = os.path.join(os.path.dirname(__file__), "model", "model.pkl")
model = joblib.load(model_path)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "Iris model auto deploy works"}

@app.post("/predict")
def predict_species(data: IrisInput):
    X = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(X)
    return {"predicted_class": int(prediction[0])}
