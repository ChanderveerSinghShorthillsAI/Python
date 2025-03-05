# Python Function Arguments - A Complete Guide

# 1. Function with Positional Arguments
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    sum_value = a + b
    print("Sum:", sum_value)

# Function Calls
add_numbers(2, 3)  # Output: Sum: 5


# 2. Function with Default Arguments
def add_numbers_default(a=7, b=8):
    """Returns the sum of two numbers with default values."""
    sum_value = a + b
    print("Sum:", sum_value)

# Function Calls
add_numbers_default(2, 3)  # Output: Sum: 5
add_numbers_default(a=2)    # Output: Sum: 10 (b=8 default)
add_numbers_default()       # Output: Sum: 15 (a=7, b=8 default)


# 3. Function with Keyword Arguments
def display_info(first_name, last_name):
    """Displays first and last name using keyword arguments."""
    print("First Name:", first_name)
    print("Last Name:", last_name)

# Function Calls
display_info(last_name="Cartman", first_name="Eric")

# Output:
# First Name: Eric
# Last Name: Cartman


# 4. Function with Arbitrary Arguments (*args)
def find_sum(*numbers):
    """Finds the sum of multiple numbers passed as arguments."""
    result = sum(numbers)
    print("Sum:", result)

# Function Calls
find_sum(1, 2, 3)   # Output: Sum: 6
find_sum(4, 9)      # Output: Sum: 13

# *args allows passing a variable number of arguments
# Internally, `numbers` behaves like a tuple


# 5. Function with Arbitrary Keyword Arguments (**kwargs)
def display_student_info(**details):
    """Displays student details using arbitrary keyword arguments."""
    for key, value in details.items():
        print(f"{key}: {value}")

# Function Calls
display_student_info(name="Alice", age=22, course="CS")

# Output:
# name: Alice
# age: 22
# course: CS


# 6. Function with Mixed Arguments (Positional, Default, *args, **kwargs)
def mixed_function(a, b=5, *args, **kwargs):
    """Demonstrates different types of function arguments."""
    print(f"Positional Arguments: a={a}, b={b}")
    print(f"Arbitrary Arguments (*args): {args}")
    print(f"Keyword Arguments (**kwargs): {kwargs}")

# Function Call
mixed_function(10, 20, 30, 40, key1="value1", key2="value2")

# Output:
# Positional Arguments: a=10, b=20
# Arbitrary Arguments (*args): (30, 40)
# Keyword Arguments (**kwargs): {'key1': 'value1', 'key2': 'value2'}

