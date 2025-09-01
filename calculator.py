import streamlit as st

# Corrected price-per-kg table
prices = {
    "Carrot": 18 / 0.1,
    "Strawberry": 14 / 0.05,
    "Aloe": 310 / 1.5,
    "Blueberry": 23 / 0.01,
    "Apple": 73 / 0.18,
    "Tulip": 767 / 0.01,
    "Daffodil": 1090 / 0.01,
    "Corn": 36 / 1.2,
    "Watermelon": 2708 / 4.5,
    "Pumpkin": 3700 / 6.0,
    "Echeveria": 5520 / 0.8,
    "Coconut": 302 / 5.0,
    "Banana": 1750 / 0.12,
    "Lily": 20123 / 0.02,
    "Burro's Tail": 6000 / 0.4,
    "Mushroom": 160000 / 25.0,
    "Cactus": 287000 / 1500.0,
    "Bamboo": 500000 / 1.0,
    "Grape": 7220 / 3.0,
    "Pepper": 7220 / 0.5,
    "Lemon": 10000 / 0.5,
    "Passion Fruit": 24500 / 9.5,
    "Dragon Fruit": 24500 / 8.4,
    "Lychee": 50000 / 9.0,
    "Sunflower": 750000 / 10.0,
    "Starweaver": 10000000 / 10.0
}

mutations = {
    "None": 1,
    "Golden": 25,
    "Rainbow": 50
}

weather = ["None", "Wet", "Chilled", "Frozen", "Dawnlit", "Ambershine"]

combined_weather = {
    ("Wet", "Dawnlit"): 3,
    ("Chilled", "Dawnlit"): 3,
    ("Wet", "Ambershine"): 6,
    ("Chilled", "Ambershine"): 6,
    ("Frozen", "Dawnlit"): 11,
    ("Frozen", "Ambershine"): 14
}

st.title("Crop Sell Price Calculator with Mutations & Weather")

# Crop selection
crop = st.selectbox("Select a crop", list(prices.keys()))

# Weight input
weight = st.number_input("Enter weight (kg)", min_value=0.01, value=1.0, step=0.01)

# Mutation selection
mutation = st.selectbox("Select mutation", list(mutations.keys()))

# Weather selections
weather_base = st.selectbox("Select base weather", weather)
weather_special = st.selectbox("Select special weather", ["None", "Dawnlit", "Ambershine"])

# Calculate button
if st.button("Calculate"):
    price = prices[crop] * weight
    
    # Apply mutation
    price *= mutations[mutation]
    
    # Apply weather multiplier
    if weather_base != "None" and weather_special != "None":
        price *= combined_weather.get((weather_base, weather_special), weather[weather_base] * weather[weather_special])
    elif weather_base != "None":
        price *= weather[weather_base]
    elif weather_special != "None":
        price *= weather[weather_special]
    
    st.success(f"{crop} ({weight:.2f} kg) with {mutation} mutation and weather {weather_base}/{weather_special} sells for {price:,.0f} coins")
