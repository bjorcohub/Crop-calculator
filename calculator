import streamlit as st

# Price per kg table
prices = {
    "Carrot": 100,
    "Strawberry": 1000,
    "Aloe": 90,
    "Blueberry": 40000,
    "Apple": 2777.78,
    "Tulip": 60000,
    "Tomato": 2666.67,
    "Daffodil": 100000,
    "Corn": 1083.33,
    "Watermelon": 555.56,
    "Pumpkin": 500,
    "Echeveria": 5250,
    "Coconut": 1200,
    "Banana": 62500,
    "Lily": 1000000,
    "Burro's Tail": 232500,
    "Mushroom": 6000,
    "Cactus": 166.67,
    "Bamboo": 400000,
    "Grape": 2833.33,
    "Pepper": 2000000,
    "Lemon": 4000000,
    "Passion Fruit": 289473.68,
    "Dragon Fruit": 595238.1,
    "Lychee": 2777777.78,
    "Sunflower": 10000000,
    "Starweaver": 100000000
}

st.title("Crop Sell Price Calculator")

# Dropdown for crop
crop = st.selectbox("Select a crop", list(prices.keys()))

# Input for weight
weight = st.number_input("Enter weight (kg)", min_value=0.01, value=1.0, step=0.1)

# Calculate button
if st.button("Calculate"):
    price = prices[crop] * weight
    st.success(f"{crop} ({weight:.2f} kg) sells for {price:,.0f} coins")
