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


def cause_plant_error():
    raise PlantError("The tomato plant is wilting!")


def cause_plant_error_none():
    raise PlantError()


def cause_water_error():
    raise WaterError("Not enough water in the tank!")


def cause_water_error_none():
    raise WaterError()


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        cause_plant_error()
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!")

    print("\nTesting WaterError...")
    try:
        cause_water_error()
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!")

    print("\nTesting catching all garden errors...")
    try:
        cause_plant_error()
    except GardenError:
        print("Caught PlantError: The tomato plant is wilting!")
    try:
        cause_water_error()
    except GardenError:
        print("Caught WaterError: Not enough water in the tank!")

    print("\nAll custom error types work correctly!")
"""
    try:
        cause_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        cause_plant_error_none()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
"""

if __name__ == "__main__":
    test_custom_errors()
