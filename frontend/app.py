import streamlit as st
import requests

# Streamlit app
st.title("Merchandising Prediction Dashboard")

# Input form for product features
st.header("Enter Product Features for Demand Prediction")

price = st.number_input("Price", min_value=100.0, max_value=3000.0, step=50.0)
rating = st.slider("Rating", min_value=0.0, max_value=5.0, step=0.1)
reviews = st.number_input("Reviews", min_value=1, max_value=10000, step=1)
review_growth_rate = st.number_input("Review Growth Rate", min_value=0.0, max_value=1.0, step=0.01)
cotton = st.radio("Is it made of Cotton?", [0, 1])
polyester = st.radio("Is it made of Polyester?", [0, 1])
round_neck = st.radio("Has Round Neck?", [0, 1])
polo_neck = st.radio("Has Polo Neck?", [0, 1])
short_sleeve = st.radio("Has Short Sleeve?", [0, 1])
long_sleeve = st.radio("Has Long Sleeve?", [0, 1])

# Button to make the prediction
if st.button("Predict Demand"):
    # Create a request payload
    payload = {
        "price": price,
        "rating": rating,
        "reviews": reviews,
        "review_growth_rate": review_growth_rate,
        "Cotton": cotton,
        "Polyester": polyester,
        "Round_Neck": round_neck,
        "Polo_Neck": polo_neck,
        "Short_Sleeve": short_sleeve,
        "Long_Sleeve": long_sleeve
    }
    
    # Make API call to FastAPI backend
    response = requests.post("http://localhost:8000/predict", json=payload)
    
    # Display the predicted demand
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Reviews (Demand): {result['predicted_reviews']}")
    else:
        st.error("Prediction failed. Please try again.")
