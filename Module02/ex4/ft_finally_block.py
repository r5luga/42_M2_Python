#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, mesg="Unknown garden error"):
        super().__init__(mesg)


class PlantError(GardenError):
    def __init__(self, mesg=None):
        if mesg == None:
            mesg = "Unknown plant error"
        super().__init__(mesg)


class WaterError(GardenError):
    def __init__(self, mesg=None):
        if mesg == None:
            mesg = "Unknown water error"
        super().__init__(mesg)


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"{plant_name}")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: Invalid plant name to water: '{e}'")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: Invalid plant name to water: '{e}'")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
