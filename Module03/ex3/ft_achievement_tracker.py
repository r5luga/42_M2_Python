#!/usr/bin/env python3
#!/usr/bin/env python3
import random


ALL_ACHIEVEMENTS: list[str] = [
    "Boss Slayer",
    "Collector Supreme",
    "Crafting Genius",
    "First Steps",
    "Hidden Path Finder",
    "Master Explorer",
    "Sharp Mind",
    "Speed Runner",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Unstoppable",
    "Untouchable",
    "World Savior"
    ]


def gen_player_achievements() -> set[str]:
    total: int = len(ALL_ACHIEVEMENTS)

    count: int = random.randint(5, 9)

    chosen: set[str] = set()
    while len(chosen) < count:
        chosen.add(random.choice(ALL_ACHIEVEMENTS))

    return chosen


def my_achievement_tracker() -> None:
    """
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }
    """
    players: dict[str, set[str]] = {}
    
    players["Alice"] = {
        "Boss Slayer",
        "Collector Supreme",
        "Crafting Genius",
        "Master Explorer",
        "Untouchable",
        "World Savior"
        }
    players["Bob"] = {
        "Collector Supreme",
        "Crafting Genius",
        "Master Explorer",
        "Strategist",
        "Unstoppable",
        "Untouchable",
        "World Savior"
        }
    players["Charlie"] = {
        "Collector Supreme",
        "First Steps",
        "Master Explorer",
        "Sharp Mind",
        "Speed Runner",
        "Strategist",
        "Survivor",
        "Treasure Hunter",
        "Untouchable"
        }
    players["Dylan"] = {
        "Boss Slayer",
        "Speed Runner",
        "Strategist",
        "Unstoppable",
        "Untouchable"
        }

    for name, achievement in players.items():
        print(f"Player {name}: {achievement}")

    all_distinct: set[str] = set.union(*players.values())
    print(f"All distinct achievements: {all_distinct}")

    common: set[str] = set.intersection(*players.values())
    print(f"Common achievements: {common}")

    for name, achievement in players.items():
        others_union: set[str] = set.union(
            *(v for k, v in players.items() if k != name)
        )
        unique_to_player: set[str] = achievement.difference(others_union)
        print(f"Only {name} has: {unique_to_player}")

    for name, achievement in players.items():
        # missing: set[str] = all_distinct.difference(achievement)
        missing: set[str] = set(ALL_ACHIEVEMENTS).difference(achievement)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    my_achievement_tracker()
