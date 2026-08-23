#!/usr/bin/env python3

def input_temperature(temp_str):
    return int(temp_str)
    
def test_temperature():
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    var_input = "25"
    try:
        temperature = input_temperature(var_input)
        print(f"Temperature is now {temperature}°C")
    except Exception:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{var_input}'")

    print("\nInput data is 'abc'")
    var_input = "abc"
    try:
        temperature = input_temperature(var_input)
        print(f"Temperature is now {temperature}°C")
    except Exception:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{var_input}'")
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
