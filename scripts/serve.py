
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/predict")
def predict(a: float, b: float, c: float):
    pred = model.predict(np.array([[a, b, c]]))
    return {"prediction": int(pred[0])}
