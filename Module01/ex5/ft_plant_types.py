#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 10.0
            print(f"Value defaulted to {self._height}")
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 1
            print(f"Value defaulted to {self._age}")
        else:
            self._age = age

    def show(self) -> None:
        print(
            f"{self._name}: "
            f"{round(self.get_height(), 1):.1f}cm, "
            f"{self.get_age()} days old"
        )

    def __str__(self) -> str:
        return (
            f"{self._name}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def set_height(self, height: float) -> int:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return 0
        else:
            self._height = height
            return 1

    def set_age(self, age: int) -> int:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return 0
        else:
            self._age = age
            return 1

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str = "red"
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = 0

    def bloom(self) -> None:
        self._blooming = 1

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming == 1:
            print(f" {self.get_name()} is blooming beautifully!")
        else:
            print(f" {self.get_name()} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.get_name()} "
            f"now produces a shade of {self.get_height()}cm "
            f"long and {self._trunk_diameter:.1f}cm wide"
        )

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n Trunk diameter: {self._trunk_diameter:.1f}"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self, age: int) -> None:
        new_age = super().get_age() + age
        super().set_age(new_age)
        self._nutritional_value = age

    def grow(self, height: float) -> None:
        new_height = super().get_height() + height
        super().set_height(new_height)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 0.5)
    print(f"{oak}")
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()
