#Exception Handling (try / except) :Handle errors gracefully without crashing your script.

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result
safe_divide_result = safe_divide(10, 0)
print(safe_divide_result)  # Output: Error: Cannot divide by zero.

safe_divide_result = safe_divide(10, "a")
print(safe_divide_result)  # Output: Error: Invalid input type. Please provide numbers.

safe_divide_result = safe_divide(10, 5)
print(safe_divide_result)  # Output: Error: Cannot divide by zero.
