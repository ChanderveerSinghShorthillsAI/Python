# Python Functions - A Complete Guide

# 1. Basic Function Declaration & Calling
def greet():
    """Prints a greeting message."""
    print("Hello, welcome to Python functions!")

# Calling the function
greet()


# 2. Function with Parameters and Return Value
def add(num1: int, num2: int) -> int:
    """Returns the sum of two numbers."""
    return num1 + num2

# Function Call
result = add(5, 10)
print(f"Sum: {result}")


# 3. Function to Check if a Number is Prime
def is_prime(n):
    """Checks whether a number is prime."""
    if n in [2, 3]:
        return True
    if n == 1 or n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

print(is_prime(7))  # True
print(is_prime(8))  # False


# 4. Function with Default Arguments
def power(base, exponent=2):
    """Returns base raised to exponent, default is square."""
    return base ** exponent

print(power(3))    # 9 (3^2)
print(power(3, 3)) # 27 (3^3)


# 5. Keyword Arguments
def student(firstname, lastname):
    """Prints student name."""
    print(firstname, lastname)

# Calling with keyword arguments
student(firstname="John", lastname="Doe")


# 6. Positional Arguments
def name_age(name, age):
    """Prints name and age."""
    print(f"Name: {name}, Age: {age}")

name_age("Alice", 25)   # Correct
name_age(25, "Alice")   # Incorrect order


# 7. Arbitrary Arguments (*args and **kwargs)
def greet_people(*names):
    """Prints names given as arguments."""
    for name in names:
        print(f"Hello, {name}!")

greet_people("Alice", "Bob", "Charlie")

def student_info(**details):
    """Prints student details."""
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Alice", age=22, course="CS")


# 8. Function Docstring
def square_value(num):
    """Returns the square of a number."""
    return num ** 2

print(square_value.__doc__)  # Print docstring


# 9. Nested Function
def outer_function():
    """Outer function containing inner function."""
    msg = "Hello from Outer Function"

    def inner_function():
        print(msg)

    inner_function()

outer_function()


# 10. Anonymous (Lambda) Functions
cube = lambda x: x * x * x
print(cube(3))  # 27


# 11. Recursive Function (Factorial)
def factorial(n):
    """Returns factorial of a number using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))  # 24


# 12. Function Returning Multiple Values
def get_coordinates():
    """Returns multiple values as a tuple."""
    return (10.5, 22.3)

x, y = get_coordinates()
print(f"Coordinates: {x}, {y}")


# 13. Function Scope (Local vs Global Variables)
global_var = "I am global"

def check_scope():
    """Demonstrates local scope."""
    local_var = "I am local"
    print(local_var)

check_scope()
print(global_var)


# 14. Pass by Reference vs Pass by Value
def modify_list(lst):
    """Modifies the first element of the list."""
    lst[0] = 100

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [100, 2, 3]

# Example where reference is broken
def reassign(lst):
    """Assigns a new list, breaking reference."""
    lst = [4, 5, 6]

my_list = [1, 2, 3]
reassign(my_list)
print(my_list)  # [1, 2, 3] - Unchanged


# 15. Swap Function (Pass by Value)
def swap(a, b):
    """Swaps two values (Pass by Value example)."""
    temp = a
    a = b
    b = temp

x, y = 10, 20
swap(x, y)
print(x, y)  # 10 20 (Unchanged)


# 16. Function with Default Parameters
def greet_person(name="Guest"):
    """Greets the person with default name."""
    print(f"Hello, {name}!")

greet_person()        # Hello, Guest!
greet_person("Alice") # Hello, Alice!


# 17. Function with Return Statements
def square(num):
    """Returns square of a number."""
    return num ** 2

print(square(5))  # 25


# 18. Function with Arbitrary Keyword Arguments
def display_info(**info):
    """Displays key-value pairs."""
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(Name="Alice", Age=25, Country="USA")


# 19. Function Returning a Dictionary
def get_student_info():
    """Returns a dictionary with student info."""
    return {"name": "Alice", "age": 22, "course": "CS"}

student = get_student_info()
print(student["name"])  # Alice


# 20. Function Returning a List
def get_numbers():
    """Returns a list of numbers."""
    return [1, 2, 3, 4, 5]

numbers = get_numbers()
print(numbers)


# 21. Function as an Argument
def apply_function(func, value):
    """Applies a function to a value."""
    return func(value)

print(apply_function(square, 4))  # 16


# 22. Recursive Function (Fibonacci)
def fibonacci(n):
    """Returns nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # 5
