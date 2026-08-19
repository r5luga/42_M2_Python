#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
    def grow(self, height):
        self.height += height
    def older(self, age):
        self.age += age

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.show()
    cactus = Plant("Cactus", 15, 120)
    cactus.show()
    
    rose.grow(0.2)
    rose.older(1)
    
    print("=== Garden Plant Growth ===")
    rose.show()
    sunflower.show()
    cactus.show()
