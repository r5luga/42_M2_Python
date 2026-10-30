def ft_count_harvest_recursive() -> None:

    def ft_helper(i: int = 1, until: int = 1) -> None:
        print(f"Day {i}")
        if i < until:
            ft_helper(i + 1, until)

    until = int(input("Days until harvest: "))
    ft_helper(1, until)
