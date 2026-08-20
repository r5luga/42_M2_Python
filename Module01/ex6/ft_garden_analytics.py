#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self, plant):
            self._plant = plant
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
        def inc_grow(self):
            self._grow_calls += 1
        def inc_age(self):
            self._age_calls += 1
        def inc_show(self):
            self._show_calls += 1
        def display(self):
            print(f"[statistics for {self._plant.get_name()}]")
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def Anonymous(cls):
        return cls("Unknown plant", 0, 0)
        
    def __init__(self, name, height, age):
        self._stats = Plant.Stats(self)
        self._name = name
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 10
            print(f"Value defaulted to {self._height}")
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 1
            print(f"Value defaulted to {self._age}")
        else:
            self._age = age
    def show(self):
        self._stats.inc_show()
        print(f"{self._name}: {round(self.get_height(), 1):.1f}cm, {self.get_age()} days old")
    def __str__(self):
        self._stats.inc_show()
        return f"{self._name}: {self.get_height():.1f}cm, {self.get_age()} days old"
    def set_height(self, height):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return 0
        else:
            self._stats.inc_grow()
            self._height = height
            return 1
    def set_age(self, age):
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return 0
        else:
            self._stats.inc_age()
            self._age = age
            return 1
    def get_name(self):
        return self._name
    def get_height(self):
        return self._height
    def get_age(self):
        return self._age

class Flower(Plant):
    def __init__(self, name, height, age, color="red"):
        super().__init__(name, height, age)
        self._color = color
        self._blooming = 0
    def bloom(self):
        self._blooming = 1
    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._blooming == 1:
            print(f" {self.get_name()} is blooming beautifully!")
        else:
            print(f" {self.get_name()} has not bloomed yet")

class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self, plant):
            super().__init__(plant)
            self._shade_calls = 0
        def inc_shade(self):
            self._shade_calls += 1
        def display(self):
            super().display()
            print(f" {self._shade_calls} shade")
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._stats = Tree.TreeStats(self)
        self._trunk_diameter  = trunk_diameter 
    def produce_shade(self):
        self._stats.inc_shade()
        print(f"Tree {self.get_name()} now produces a shade of {self.get_height()}cm long and {self._trunk_diameter:.1f}cm wide")
    def __str__(self):
        return super().__str__() + f"\n Trunk diameter: {self._trunk_diameter:.1f}"
        
class Seed(Flower):
    def __init__(self, name, height, age, color="red"):
        super().__init__(name, height, age, color)
        self._seed_count = 0
    def bloom(self, seeds):
        super().bloom()
        # Once blooming, seeds appear
        self._seed_count = seeds
    def show(self):
        super().show()
        print(f" Seeds: {self._seed_count}")

def display_statistics(plant):
    plant._stats.display()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")

    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10)
    rose.show()
    display_statistics(rose)
    print("[asking the rose to bloom]")
    rose.set_height(23)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 0.5)
    print(f"{oak}")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.set_height(110)
    sunflower.set_age(65)
    sunflower.bloom(42)
    sunflower.show()
    display_statistics(sunflower)
    
    print("\n=== Anonymous")
    anonymous = Plant.Anonymous()
    anonymous.show()
    display_statistics(anonymous)
