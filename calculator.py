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

# Mutations multipliers
mutations = {
    "None": 1,
    "Golden": 25,
    "Rainbow": 50
}

# Weather multipliers
weather_multipliers = {
    "None": 1,
    "Wet": 2,
    "Chilled": 2,
    "Frozen": 10,
    "Dawnlit": 2,
    "Ambershine": 5
}

# Combined rules for stacking
combined_weather = {
    ("Wet", "Dawnlit"): 3,
    ("Chilled", "Dawnlit"): 3,
    ("Wet", "Ambershine"): 6,
    ("Chilled", "Ambershine"): 6,
    ("Frozen", "Dawnlit"): 11,
    ("Frozen", "Ambershine"): 14
}

# Friend bonus percentages
friend_bonus_percent = {
    "0%": 0.0,
    "10%": 0.10,
    "20%": 0.20,
    "30%": 0.30,
    "40%": 0.40,
    "50%": 0.50
}

st.title("Crop Sell Price Calculator with Mutations, Weather & Friend Bonus")

# Crop selection
crop = st.selectbox("Select a crop", list(prices.keys()))

# Weight input
weight = st.number_input("Enter weight (kg)", min_value=0.01, value=1.0, step=0.01)

# Mutation selection
mutation = st.selectbox("Select mutation", list(mutations.keys()))

# Weather selections
weather_base = st.selectbox("Select base weather", ["None", "Wet", "Chilled", "Frozen"])
weather_special = st.selectbox("Select special weather", ["None", "Dawnlit", "Ambershine"])

# Friend bonus selection
friend_bonus_choice = st.selectbox("Friend Bonus", ["0%", "10%", "20%", "30%", "40%", "50%"])

# Calculate button
if st.button("Calculate"):
    price = prices[crop] * weight
    
    # Apply mutation
    price *= mutations[mutation]
    
    # Apply weather multiplier
    if weather_base != "None" and weather_special != "None":
        price *= combined_weather.get(
            (weather_base, weather_special), 
            weather_multipliers[weather_base] * weather_multipliers[weather_special]
        )
    elif weather_base != "None":
        price *= weather_multipliers[weather_base]
    elif weather_special != "None":
        price *= weather_multipliers[weather_special]
    
    # Apply friend bonus
    price *= (1 + friend_bonus_percent[friend_bonus_choice])
    
    st.success(f"{crop} ({weight:.2f} kg) with {mutation} mutation, weather {weather_base}/{weather_special}, "
               f"and friend bonus {friend_bonus_choice} sells for {price:,.0f} coins")
