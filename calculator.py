import streamlit as st

# Price per kg table
prices = {
    "Carrot": 18 / 0.1,          # 180
    "Strawberry": 14 / 0.05,     # 280
    "Aloe": 310 / 1.5,           # 206.67
    "Blueberry": 23 / 0.01,      # 2300
    "Apple": 73 / 0.18,          # 405.56
    "Tulip": 767 / 0.01,         # 76700
    "Daffodil": 1090 / 0.01,     # 109000
    "Corn": 36 / 1.2,            # 30
    "Watermelon": 2708 / 4.5,    # 601.78
    "Pumpkin": 3700 / 6.0,       # 616.67
    "Echeveria": 5520 / 0.8,     # 6900
    "Coconut": 302 / 5.0,        # 60.4
    "Banana": 1750 / 0.12,       # 14583.33
    "Lily": 20123 / 0.02,        # 1006150
    "Burro's Tail": 6000 / 0.4,  # 15000
    "Mushroom": 160000 / 25.0,   # 6400
    "Cactus": 287000 / 1500.0,   # 191.33
    "Bamboo": 500000 / 1.0,      # 500000
    "Grape": 7220 / 3.0,         # 2406.67
    "Pepper": 7220 / 0.5,        # 14440
    "Lemon": 10000 / 0.5,        # 20000
    "Passion Fruit": 24500 / 9.5,# 2578.95
    "Dragon Fruit": 24500 / 8.4, # 2916.67
    "Lychee": 50000 / 9.0,       # 5555.56
    "Sunflower": 750000 / 10.0,  # 75000
    "Starweaver": 10000000 / 10.0# 1000000
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
