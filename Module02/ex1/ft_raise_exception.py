#!/usr/bin/env python3


def input_temperature(temp_str):
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(
            f"Caught input_temperature error: {temp}°C is too cold for plants (min 0°C)"
        )

    if temp > 40:
        raise ValueError(
            f"Caught input_temperature error: {temp}°C is too hot for plants (max 40°C)"
        )

    return temp


def test_temperature():
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    var_input = "25"
    try:
        temperature = input_temperature(var_input)
        print(f"Temperature is now {temperature}°C")
    except Exception as e:
        print("Caught input_temperature erro:", str(e))

    print("\nInput data is 'abc'")
    var_input = "abc"
    try:
        temperature = input_temperature(var_input)
        print(f"Temperature is now {temperature}°C")
    except Exception as e:
        print("Caught input_temperature erro:", str(e))

    print("\nInput data is '100'")
    var_input = "100"
    try:
        temperature = input_temperature(var_input)
        print(f"Temperature is now {temperature}°C")
    except Exception as e:
        print("Caught input_temperature erro:", str(e))

    print("\nInput data is '-50'")
    var_input = "-50"
    try:
        temperature = input_temperature(var_input)
        print(f"Temperature is now {temperature}°C")
    except Exception as e:
        print("Caught input_temperature erro:", str(e))

    # Exception is the base class for most built‑in errors
    # Exception is the base class for most built‑in errors, including:
    #  ValueError
    #  TypeError
    #  ZeroDivisionError
    #  RuntimeError
    #  and many others
    #  For debugging or production systems, it’s usually better to catch specific exceptions.
    # except Exception as e:
    #     print("An error occurred")
    #     print("Specific exception:", type(e).__name__)
    #     print("Message:", str(e))

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
