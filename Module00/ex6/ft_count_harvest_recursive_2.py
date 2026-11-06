# Using default parameter values
def ft_count_harvest_recursive(
    day: int = 1,
    until: int | None = None,
    ) -> None:

    if until is None:
        until = int(input("Days until harvest: "))

    print(f"Day {day}")

    if day < until:
        ft_count_harvest_recursive(day + 1, until)

def main() -> None:
    ft_count_harvest_recursive()

if __name__ == "__main__":
    main()
