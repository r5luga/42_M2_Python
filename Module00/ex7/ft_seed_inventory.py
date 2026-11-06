def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    seed_cap = seed_type.capitalize()

    if unit == "packets":
        last_word = "available"
    elif unit == "grams":
        last_word = "total"
    elif unit == "area":
        print(f"{seed_cap} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

    if unit == "packets" or unit == "grams":
        print(f"{seed_cap} seeds: {quantity} {unit} {last_word}")
