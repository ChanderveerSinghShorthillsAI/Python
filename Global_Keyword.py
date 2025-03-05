"""
Global Keyword in Python - Understanding Global Variable Modifications

This script demonstrates:
1. Accessing global variables inside functions
2. Modifying global variables using the `global` keyword
3. Handling UnboundLocalError when modifying a global variable
4. Modifying mutable global objects without using `global`
5. Using `global` keyword to assign a new object
"""

# ----------------- Basic Example of Global Keyword ----------------- #
x = 10  # Global variable

def modify_global_variable():
    """Uses global keyword to modify global variable"""
    global x  # Referencing the global variable
    x = 20  # Modifying the global variable

# Function call
modify_global_variable()
print("Modified Global Variable x:", x)  # Output: 20


# ----------------- Accessing Global Variables in a Function ----------------- #
a = 15
b = 10

def add():
    """Accesses global variables inside a function"""
    c = a + b  # Accessing global variables
    print("Sum:", c)

# Function call
add()  # Output: 25




# ----------------- Using `global` to Modify Global Variable ----------------- #
x = 15  # Global variable

def change_with_global():
    """Uses `global` keyword to modify a global variable"""
    global x
    x = x + 5  # Modifying global variable
    print("Inside Function:", x)

# Function call
change_with_global()
print("Outside Function:", x)  # Output: 20


# ----------------- Modifying Mutable Global Objects ----------------- #
numbers = [10, 20, 30]  # Global list

def modify_list():
    """Modifies global list without using `global`"""
    for i in range(len(numbers)):
        numbers[i] += 10  # Modifying list elements (mutable)

print("Before Modification:", numbers)
modify_list()
print("After Modification:", numbers)  # Output: [20, 30, 40]


# ----------------- Assigning a New List Using `global` ----------------- #
arr = [10, 20, 30]  # Global list

def assign_new_list():
    """Assigns a new list to global variable using `global` keyword"""
    global arr
    arr = [20, 30, 40]  # Assigning a new list

print("Before Assignment:", arr)
assign_new_list()
print("After Assignment:", arr)  # Output: [20, 30, 40]
