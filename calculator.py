import streamlit as st

# Corrected price-per-kg table
prices = {
    "Carrot": 18 / 0.1,
    "Strawberry": 14 / 0.05,
    "Aloe": 310 / 1.5,
    "Blueberry": 23 / 0.01,
    "Apple": 73 / 0.18,
    "Tulip": 767 / 0.01,
    "Tomato": 27 / 0.3,
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

# Base and max weights for crops
weights = {
    "Carrot": (0.1, 0.3),
    "Strawberry": (0.05, 0.1),
    "Aloe": (1.5, 3.8),
    "Blueberry": (0.01, 0.02),
    "Apple": (0.180, 0.360),
    "Tulip": (0.01, 0.30),
    "Tomato": (0.3, 0.6),
    "Daffodil": (0.01, 0.03),
    "Corn": (1.2, 2.4),
    "Watermelon": (4.5, 13.5),
    "Pumpkin": (6, 18),
    "Echeveria": (0.8, 2.2),
    "Coconut": (5, 15),
    "Banana": (0.12, 0.204),
    "Lily": (0.02, 0.055),
    "Burro's Tail": (0.4, 1.0),
    "Mushroom": (25, 87.5),
    "Cactus": (1500, 2700),
    "Bamboo": (1, 2),
    "Grape": (3, 6),
    "Pepper": (0.5, 1),
    "Lemon": (0.5, 1.5),
    "Passion Fruit": (9.5, 19),
    "Dragon Fruit": (8.4, 16.8),
    "Lychee": (9, 18),
    "Sunflower": (10, 25),
    "Starweaver": (10, 20)
}

# Mutations multipliers
mutations = {"None": 1, "Golden": 25, "Rainbow": 50}

# Weather multipliers
weather_multipliers = {
    "None": 1,
    "Wet": 2,
    "Chilled": 2,
    "Frozen": 10,
    "Dawnlit": 2,
    "Ambershine": 5
}

# Combined stacking rules
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

st.title("Crop Sell Price Calculator 🌾")

# Crop selection
crop = st.selectbox("Select a crop", list(prices.keys()))

# Get default weight from base value
base_weight, max_weight = [float(x) for x in weights[crop]]

# Weight input defaults to base value
weight = st.number_input(
    "Enter weight (kg)", 
    min_value=float(base_weight), 
    max_value=float(max_weight), 
    value=float(base_weight), 
    step=0.01
)


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
    
    # Apply weather multipliers
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
    
    st.success(
        f"{crop} ({weight:.2f} kg, range {base_weight}-{max_weight} kg) "
        f"with {mutation} mutation, weather {weather_base}/{weather_special}, "
        f"and friend bonus {friend_bonus_choice} sells for {price:,.0f} coins"
    )
