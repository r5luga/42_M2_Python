#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts: list[str] = raw.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except Exception as e:
            for p in parts:
                try:
                    float(p.strip())
                except Exception:
                    print(f"Error on parameter '{p.strip()}': {e}")
                    break
            continue


def distance_3d(
    pa: tuple[float, float, float], pb: tuple[float, float, float]
) -> float:
    return math.sqrt((pb[0] - pa[0]) ** 2 + (pb[1] - pa[1]) ** 2 + (pb[2] - pa[2]) ** 2)


def byebye() -> None:
    print("ByeBye!!!")


def my_coordinate_system() -> None:
    print("\nGet a first set of coordinates")
    point_a: tuple[float, float, float] = get_player_pos()
    if point_a == (0.0, 0.0, 0.0):
        return byebye()
    print(f"Got a first tuple: {point_a}")
    print(f"It includes: X={point_a[0]}, Y={point_a[1]}, Z={point_a[2]}")
    dist_center: float = distance_3d(point_a, (0.0, 0.0, 0.0))
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    point_b: tuple[float, float, float] = get_player_pos()
    if point_b == (0.0, 0.0, 0.0):
        return byebye()
    distance: float = distance_3d(point_a, point_b)
    print(f"Distance between the 2 sets of coordinates:: {round(distance, 4)}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    my_coordinate_system()
