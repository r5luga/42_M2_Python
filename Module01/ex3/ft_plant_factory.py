#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.initialheight = height
        self.initialage = age
    def show(self):
        print(f"{self.name}: {round(self.height, 1):.1f}cm, {self.age} days old")
    def __str__(self):
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"
    def grow(self, height):
        self.height += height
    def older(self, age):
        self.age += age

def create_plants(plant_list: list[dict]):
    new_plants = []
    for plant in plant_list:
        new_plants += [Plant(plant['name'], plant['height'], plant['age'])]
        # new_plants.append(Plant(**plant))
    return new_plants
    # return [Plant(plant['name'], plant['height'], plant['age']) for plant in plant_list]

if __name__ == "__main__":
    plants = create_plants([
        {'name': 'Rose', 'height': 25, 'age': 30},
        {'name': 'Oak', 'height': 200, 'age': 365},
        {'name': 'Cactus', 'height': 5, 'age': 90},
        {'name': 'Sunflower', 'height': 80, 'age': 45},
        {'name': 'Fern', 'height': 15, 'age': 120}])
        
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created :", end=" ")
        plant.show()
    # for plant in plants:
        # print(f"Created : {plant}")
