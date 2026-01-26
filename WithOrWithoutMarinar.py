import random

# -------------------------------
# Weather Generator
# -------------------------------
def random_weather():
    """
    Selects and returns a random weather condition.
    """
    weather_conditions = [
        "Sunny",
        "Partly Cloudy",
        "Cloudy",
        "Rainy",
        "Stormy",
        "Snowy",
        "Foggy"
    ]

    return random.choice(weather_conditions)

# -------------------------------
# Talking Car System
# -------------------------------
def car_advice():
    """
    Simulates a car giving driving advice based on weather conditions.
    """
    speed_limit = 65  # Speed limit in miles per hour
    weather = random_weather()

    print("\n🚗 Car System Online")
    print(f"📡 Weather sensors detect: {weather}")
    print(f"🛣️ Posted speed limit: {speed_limit} mph")

    if weather == "Sunny":
        recommended_speed = speed_limit
        print(f"☀️ Conditions are ideal. Drive at {recommended_speed} mph.")

    elif weather in ["Partly Cloudy", "Cloudy"]:
        recommended_speed = int(speed_limit * 0.9)
        print(f"🌤️ Conditions are good. Recommend {recommended_speed} mph.")

    elif weather == "Rainy":
        recommended_speed = int(speed_limit * 0.75)
        print(f"🌧️ Wet roads detected. Recommend {recommended_speed} mph.")

    elif weather in ["Foggy", "Snowy"]:
        recommended_speed = int(speed_limit * 0.6)
        print(f"🌫️ Reduced visibility or traction. Recommend {recommended_speed} mph.")

    else:  # Stormy
        recommended_speed = int(speed_limit * 0.4)
        print(f"⛈️ Severe weather! Reduce speed to {recommended_speed} mph.")

    return recommended_speed

# -------------------------------
# Run the System
# -------------------------------
car_advice()
