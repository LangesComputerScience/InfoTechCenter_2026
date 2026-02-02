#Gasoline Branch
import random

# -------------------------------------------------
# Gas Level Sensor
# -------------------------------------------------
def get_gas_level():
    """
    Simulates reading the car's gas level.
    Returns a float value between 0.0 and 1.0
    where 1.0 = full tank and 0.0 = empty.
    """
    gas_level = round(random.uniform(0.05, 1.0), 2)
    print(f"⛽ Current gas level: {int(gas_level * 100)}%")
    return gas_level


# -------------------------------------------------
# Gas Requirement Check
# -------------------------------------------------
def needs_gas(gas_level):
    """
    Determines whether the car needs gas.
    If gas is below 25%, return True.
    """
    if gas_level < 0.25:
        print("⚠️ Gas level below 1/4 tank.")
        return True
    else:
        print("✅ Gas level is sufficient.")
        return False


# -------------------------------------------------
# Gas Station Database
# -------------------------------------------------
def get_gas_stations():
    """
    Returns a list of gas stations.
    Each station is represented as a dictionary
    containing price and amenities.
    """
    return [
        {"name": "Speedy Fuel", "price": 3.59, "snacks": True, "slurpees": False},
        {"name": "QuickStop", "price": 3.49, "snacks": True, "slurpees": True},
        {"name": "Fuel Depot", "price": 3.39, "snacks": False, "slurpees": False},
        {"name": "MegaMart Gas", "price": 3.55, "snacks": True, "slurpees": True}
    ]


# -------------------------------------------------
# Best Gas Station Selector
# -------------------------------------------------
def choose_best_station(stations):
    """
    Chooses the best gas station based on:
    1. Lowest price
    2. Snacks availability
    3. Slurpees availability (highest priority)
    """
    # Sort stations based on amenities and price
    best_station = sorted(
        stations,
        key=lambda s: (s["price"], not s["slurpees"], not s["snacks"])
    )[0]

    print("\n🏁 Best Gas Station Selected:")
    print(f"📍 {best_station['name']}")
    print(f"💲 Price per gallon: ${best_station['price']}")
    print(f"🍿 Snacks available: {best_station['snacks']}")
    print(f"🥤 Slurpees available: {best_station['slurpees']}")

    return best_station


# -------------------------------------------------
# Phone Alarm Update (Simulation)
# -------------------------------------------------
def update_phone_alarm(minutes_early):
    """
    Simulates updating the user's phone alarm.
    """
    print("\n📱 Phone Alert:")
    print("⏰ Alarm Updated")
    print(f"🚨 Wake up {minutes_early} minutes earlier to get gas.")
    print("✅ Alarm successfully updated (simulation)")


# -------------------------------------------------
# Main Car Fuel Management System
# -------------------------------------------------
def gasoline_system():
    """
    Coordinates all gasoline-related functions.
    Acts as the main system controller.
    """
    print("\n🚗 Gasoline System Online")

    gas_level = get_gas_level()

    if needs_gas(gas_level):
        stations = get_gas_stations()
        best_station = choose_best_station(stations)

        # Estimate extra time needed to stop for gas
        update_phone_alarm(minutes_early=15)

        print("\n🧭 Navigation updated:")
        print(f"➡️ Routing to {best_station['name']} for refueling.")

    else:
        print("\n🟢 No gas stop required. Proceed as planned.")


# -------------------------------------------------
# Run the Program
# -------------------------------------------------
gasoline_system()
