from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

NAME = "Tanishq Singh"
ROLL_NO = "2022BCS0183"

# ✅ Define request schema
class InputData(BaseModel):
    features: list

@app.get("/")
def health():
    return {
        "name": NAME,
        "roll_no": ROLL_NO
    }

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])

    return {
        "prediction": str(prediction[0]),
        "name": NAME,
        "roll_no": ROLL_NO
    }