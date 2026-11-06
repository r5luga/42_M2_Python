# Using a separate helper function called by your main function
def ft_helper(i: int = 1, until: int = 1) -> None:
    print(f"Day {i}")
    if i < until:
        ft_helper(i + 1, until)

def ft_count_harvest_recursive() -> None:
    until = int(input("Days until harvest: "))
    ft_helper(1, until)

def main() -> None:
    ft_count_harvest_recursive()

if __name__ == "__main__":
    main()