#!/usr/bin/env python3


def garden_operations(operation_number):

    if operation_number == 0:
        return int("abc")
    elif operation_number == 1:
        return 10 / 0
    elif operation_number == 2:
        return open("/non/existent/file")
    elif operation_number == 3:
        return "plants" + 1
    else:
        return "Operation completed successfully"


def test_error_types():
    print("=== Garden Error Types Demo ===")

    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            result = garden_operations(op)
            print("Operation completed successfully")
        except ValueError:
            print("Caught ValueError: invalid literal for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print(
                "Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'"
            )
        except TypeError:
            print("Caught TypeError: can only concatenate str (not " "int" ") to str")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
