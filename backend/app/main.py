from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from .model import predict_demand

# Define FastAPI app
app = FastAPI()

# Load the model
model_path = "backend/data/model.joblib"
model = joblib.load(model_path)

# Define request schema
class ProductFeatures(BaseModel):
    price: float
    rating: float
    reviews: int
    review_growth_rate: float
    Cotton: int
    Polyester: int
    Round_Neck: int
    Polo_Neck: int
    Short_Sleeve: int
    Long_Sleeve: int

# Prediction endpoint
@app.post("/predict")
def predict(features: ProductFeatures):
    data = pd.DataFrame([features.dict()])
    prediction = predict_demand(model, data)
    return {"predicted_reviews": prediction}
