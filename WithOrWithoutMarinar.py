#BetaTestDev

# Welcome Branch
# This program simulates a simple operating system boot sequence
# with animated loading text and colored terminal output.

# -------------------------------
# Libraries Imported Here
# -------------------------------
import sys      # Used to write text to the terminal without adding new lines
import time     # Used to add delays (sleep) for animation timing

# -------------------------------
# ANSI Color Codes
# These codes change text color/style in the terminal
# -------------------------------
RESET = "\033[0m"    # Resets text color back to default
BOLD = "\033[1m"     # Makes text bold
CYAN = "\033[36m"    # Cyan text color
YELLOW = "\033[33m"  # Yellow text color
GREEN = "\033[32m"   # Green text color

# -------------------------------
# Program Title / Header
# -------------------------------
print(f"\n{BOLD}{CYAN}Welcome Branch - Developer: Mr. Lange{RESET}")
print(f"\n{BOLD}{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# -------------------------------
# Variables for Boot Animation
# -------------------------------
x = 0            # Controls how long the boot sequence runs
ellipsis = 0     # Controls the number of dots displayed during loading

# -------------------------------
# Boot Sequence Loop
# -------------------------------
# Runs until x reaches 20, simulating a system startup process
while x != 20:
    x += 1

    # Create the animated boot message with increasing dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    # Write the message on the same line (no new line)
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause briefly to control animation speed
    time.sleep(0.5)

    # Reset dots after reaching 3 to loop the animation
    if ellipsis == 4:
        ellipsis = 0

    # Final success message when boot sequence completes
    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")




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
