import random
# The random library is used to randomly select weather conditions

# -------------------------------------------------
# Weather Generator Function
# -------------------------------------------------
def random_weather():
    """
    Chooses and returns a random weather condition from a list.
    This simulates a weather sensor or weather service.
    """

    # List of possible weather conditions
    weather_conditions = [
        "Sunny",
        "Partly Cloudy",
        "Cloudy",
        "Rainy",
        "Stormy",
        "Snowy",
        "Foggy"
    ]

    # Randomly select and return one weather condition from the list
    return random.choice(weather_conditions)

# -------------------------------------------------
# Simulated Phone Notification Function
# -------------------------------------------------
def send_phone_alert(weather, delay_minutes):
    """
    Simulates sending a weather alert to a phone and
    updating the user's alarm time based on road conditions.
    
    Parameters:
    weather (str): The current weather condition
    delay_minutes (int): How many minutes earlier the alarm should be set
    """

    # Display a simulated phone notification message
    print("\n📱 Phone Notification:")
    print("⚠️ Weather Alert Received")
    print(f"🌦️ Current conditions: {weather}")

    # Inform the user that their alarm has been adjusted
    print(f"⏰ Alarm updated: Wake up {delay_minutes} minutes earlier")

    # Confirmation message (simulation only)
    print("✅ Alarm successfully updated (simulation)")

# -------------------------------------------------
# Talking Car System Function
# -------------------------------------------------
def car_advice():
    """
    Simulates a smart car system that:
    - Detects weather conditions
    - Recommends a safe driving speed
    - Determines if the driver should leave earlier
    - Sends a simulated phone alert if needed
    """

    # Posted speed limit for the road (miles per hour)
    speed_limit = 65

    # Get a random weather condition
    weather = random_weather()

    # Display system startup messages
    print("\n🚗 Car System Online")
    print(f"📡 Weather sensors detect: {weather}")
    print(f"🛣️ Posted speed limit: {speed_limit} mph")

    # Check weather conditions and adjust driving recommendations
    if weather == "Sunny":
        # Best possible driving conditions
        recommended_speed = speed_limit
        delay = 0
        print(f"☀️ Conditions are ideal. Drive at {recommended_speed} mph.")

    elif weather in ["Partly Cloudy", "Cloudy"]:
        # Slightly reduced visibility or lighting
        recommended_speed = int(speed_limit * 0.9)
        delay = 5
        print(f"🌤️ Conditions are fair. Recommend {recommended_speed} mph.")

    elif weather == "Rainy":
        # Wet roads increase stopping distance
        recommended_speed = int(speed_limit * 0.75)
        delay = 10
        print(f"🌧️ Wet roads detected. Recommend {recommended_speed} mph.")

    elif weather in ["Foggy", "Snowy"]:
        # Reduced visibility or traction
        recommended_speed = int(speed_limit * 0.6)
        delay = 20
        print(f"🌫️ Poor visibility or traction. Recommend {recommended_speed} mph.")

    else:  # Stormy
        # Severe weather conditions
        recommended_speed = int(speed_limit * 0.4)
        delay = 30
        print(f"⛈️ Severe weather detected! Recommend {recommended_speed} mph.")

    # If bad weather will slow travel, notify the phone
    if delay > 0:
        send_phone_alert(weather, delay)
    else:
        print("📱 No alarm update needed. Drive safely!")

    # Return the recommended speed in case it is needed elsewhere
    return recommended_speed

# -------------------------------------------------
# Run the Simulation
# -------------------------------------------------
# Start the car advice system
car_advice()
