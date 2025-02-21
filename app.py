import streamlit as st
import requests

def get_location_names():
    BACKEND_URL = "https://bengaluru-house-price-prediction-q8yf.onrender.com"
    response = requests.get(f"{BACKEND_URL}/get_location_names")
    if response.status_code == 200:
        return response.json()['locations']
    return []

def estimate_price(sqft, bhk, bath, location):
    data = {'total_sqft': sqft, 'bhk': bhk, 'bath': bath, 'location': location}
    BACKEND_URL = "https://bengaluru-house-price-prediction-q8yf.onrender.com"
    response = requests.post(f"{BACKEND_URL}/predict_home_price", data=data)
    if response.status_code == 200:
        return response.json()['estimated_price']
    return "Error"

st.set_page_config(page_title="Bangalore Home Price Prediction", layout="centered")
st.markdown("""<style>
    .stApp {background: url('https://source.unsplash.com/1600x900/?luxury,villa') no-repeat center center fixed;
            background-size: cover;}
</style>""", unsafe_allow_html=True)

st.markdown("## :house: Bangalore House Price Predictor", unsafe_allow_html=True)

sqft = st.text_input("**Area (Square Feet)**", "1000")

bhk = st.radio("**BHK**", [1, 2, 3, 4, 5], index=2, horizontal=True)

bath = st.radio("**Bath**", [1, 2, 3, 4, 5], index=3, horizontal=True)

locations = get_location_names()
location = st.selectbox("**Location**", ["Choose a Location"] + locations)

if st.button("Estimate Price", use_container_width=True):
    if location == "Choose a Location":
        st.warning("Please select a valid location.")
    else:
        price = estimate_price(float(sqft), bhk, bath, location)
        st.success(f"Estimated Price: ₹ {price} Lakhs")
