#Weather Branch

import random

def random_weather():
    """
    Returns and prints a random weather condition.
    """
    weather_conditions = [
        "Sunny ☀️",
        "Partly Cloudy 🌤️",
        "Cloudy ☁️",
        "Rainy 🌧️",
        "Stormy ⛈️",
        "Snowy ❄️",
        "Windy 🌬️",
        "Foggy 🌫️"
    ]

    weather = random.choice(weather_conditions)
    print(f"Today's weather is: {weather}")
    return weather

random_weather()