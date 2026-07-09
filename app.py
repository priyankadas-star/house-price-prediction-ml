import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="House Price Prediction", layout="wide")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Model
model = joblib.load("house_price_model.pkl")

# Title
st.title("🏠 House Price Prediction")
st.write("Predict California House Prices using Machine Learning")

# ==========================
# REPLACE YOUR OLD INPUTS WITH THIS
# ==========================

st.subheader("🏠 House Details")

col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("Longitude", value=-122.23)
    latitude = st.number_input("Latitude", value=37.88)
    housing_median_age = st.number_input("Housing Median Age", value=30)
    median_income = st.number_input("Median Income", value=5.0)

with col2:
    total_rooms = st.number_input("Total Rooms", value=1000)
    total_bedrooms = st.number_input("Total Bedrooms", value=200)
    population = st.number_input("Population", value=500)
    households = st.number_input("Households", value=150)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)

# ==========================
# Prediction
# ==========================

if st.button("Predict House Price"):

    input_df = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })

    prediction = model.predict(input_df)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")