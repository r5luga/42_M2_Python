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
        return f"{self._name}: {self.get_height():.1f}cm, "
        f"{self.get_age()} days old"

    def set_height(self, height: float) -> int:
        if height < 0.0:
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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print(f"Plant created: {rose}\n")

    rose.set_height(25)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days\n")

    if rose.set_height(-1) == 1:
        print(f"Height updated: {rose.get_height()}cm")
    if rose.set_age(-1) == 1:
        print(f"Age updated: {rose.get_age()}cm")

    print(f"\nCurrent state: {rose}")
