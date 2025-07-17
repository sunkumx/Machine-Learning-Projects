from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

@app.get("/")
def home():
    return {"message": "Iris Classifier is running."}

@app.post("/predict")
def predict(features: list):
    features_array = np.array(features).reshape(1, -1)
    scaled = scaler.transform(features_array)
    prediction = model.predict(scaled)
    return {"predicted_class": int(prediction[0])}
