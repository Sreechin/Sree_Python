#Functions in Python are reusable blocks of code designed to perform a specific task. They make code modular, easier to read, and simpler to debug by avoiding repetition.

# def greet(name):
#     """ This function takes name and prints greeting message"""
#     print(f"Hello, {name}! Welcome to Python programming.")


def add_numbers(a, b):
    """ This fucntion is used for adding two numbers and retrurning results"""
    Total = a + b
    return Total

Total = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {Total}")
