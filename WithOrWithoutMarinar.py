import random

# -------------------------------
# Weather Generator
# -------------------------------
def random_weather():
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
# Simulated Phone Notification
# -------------------------------
def send_phone_alert(weather, delay_minutes):
    """
    Simulates sending a message to your phone and updating your alarm.
    """
    print("\n📱 Phone Notification:")
    print("⚠️ Weather Alert Received")
    print(f"🌦️ Current conditions: {weather}")
    print(f"⏰ Alarm updated: Wake up {delay_minutes} minutes earlier")
    print("✅ Alarm successfully updated (simulation)")

# -------------------------------
# Talking Car System
# -------------------------------
def car_advice():
    speed_limit = 65  # mph
    weather = random_weather()

    print("\n🚗 Car System Online")
    print(f"📡 Weather sensors detect: {weather}")
    print(f"🛣️ Posted speed limit: {speed_limit} mph")

    if weather == "Sunny":
        recommended_speed = speed_limit
        delay = 0
        print(f"☀️ Conditions are ideal. Drive at {recommended_speed} mph.")

    elif weather in ["Partly Cloudy", "Cloudy"]:
        recommended_speed = int(speed_limit * 0.9)
        delay = 5
        print(f"🌤️ Conditions are fair. Recommend {recommended_speed} mph.")

    elif weather == "Rainy":
        recommended_speed = int(speed_limit * 0.75)
        delay = 10
        print(f"🌧️ Wet roads detected. Recommend {recommended_speed} mph.")

    elif weather in ["Foggy", "Snowy"]:
        recommended_speed = int(speed_limit * 0.6)
        delay = 20
        print(f"🌫️ Poor visibility or traction. Recommend {recommended_speed} mph.")

    else:  # Stormy
        recommended_speed = int(speed_limit * 0.4)
        delay = 30
        print(f"⛈️ Severe weather detected! Recommend {recommended_speed} mph.")

    # If weather causes a delay, notify the phone
    if delay > 0:
        send_phone_alert(weather, delay)
    else:
        print("📱 No alarm update needed. Drive safely!")

    return recommended_speed

# -------------------------------
# Run the Simulation
# -------------------------------
car_advice()
