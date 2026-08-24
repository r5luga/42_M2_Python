#!/usr/bin/env python3
import sys


def my_quest() -> None:
    program_name: str
    total_args: int
    arg_count: int
    argument: str

    program_name = sys.argv[0]
    print(f"Program name: {program_name}")

    total_args = len(sys.argv)
    if total_args == 1:
        print("No arguments provided!")
        print(f"Total arguments: {total_args}")
        return

    arg_count = total_args - 1
    print(f"Arguments received: {arg_count}")

    for i in range(1, total_args):
        argument = sys.argv[i]
        print(f"Argument {i}: {argument}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    my_quest()
