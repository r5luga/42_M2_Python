#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
    def grow(self, height):
        self.height += height
    def older(self, age):
        self.age += age

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25, 30)
    plant.show()
    
# Simulate 7 days of growth
    daily_growth = 0.8   # cm per day
    initial_height = plant.height

    for day in range(1, 8):
        plant.grow(daily_growth)
        plant.older(1)
        print(f"=== Day {day} ===")
        plant.show()
    
    total_increase = plant.height - initial_height
    print(f"Growth this week: {round(total_increase, 1)}cm")
