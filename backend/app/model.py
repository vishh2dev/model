import pandas as pd
from xgboost import XGBRegressor

# Function to predict demand (reviews)
def predict_demand(model, data: pd.DataFrame):
    prediction = model.predict(data)
    return prediction[0]
