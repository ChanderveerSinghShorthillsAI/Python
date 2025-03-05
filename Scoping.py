"""
Python Scope of Variables - Understanding Local and Global Scope

This script demonstrates:
1. Local Variables
2. Global Variables
3. Global and Local Variables with the Same Name
4. Using `global` Keyword to Modify Global Variables
5. UnboundLocalError Example
"""

# ----------------- Local Variable Example ----------------- #
def local_scope_example():
    """Demonstrates local variable scope"""
    message = "I love GeeksforGeeks"
    print("Inside Function:", message)

# Function call
local_scope_example()

# Uncommenting this line will raise an error
# print(message)  # NameError: name 'message' is not defined


# ----------------- Global Variable Example ----------------- #
# Global variable
message = "I love GeeksforGeeks"

def global_scope_example():
    """Demonstrates accessing global variables"""
    print("Inside Function:", message)

# Function call
global_scope_example()

# Accessing global variable outside the function
print("Outside Function:", message)


# ----------------- Global and Local Variables with the Same Name ----------------- #
message = "I love GeeksforGeeks"

def variable_shadowing_example():
    """Local variable with same name as global variable"""
    message = "Me too."
    print("Inside Function:", message)

# Function call
variable_shadowing_example()

# Accessing global variable outside the function
print("Outside Function:", message)


# ----------------- UnboundLocalError Example ----------------- #
message = "I love GeeksforGeeks"

def unbound_local_error():
    """Demonstrates UnboundLocalError"""
    # print(message)  # Error: message is referenced before assignment
    message = "Me too."  # Creates a new local variable
    print("Inside Function:", message)

# Function call
unbound_local_error()
print("Outside Function:", message)


# ----------------- Using `global` Keyword to Modify Global Variables ----------------- #
message = "Python is great!"

def modify_global():
    """Using global keyword to modify global variables"""
    global message
    print("Before Modification:", message)
    message = "Look for GeeksforGeeks Python Section"
    print("After Modification:", message)

# Function call
modify_global()
print("Outside Function:", message)


# ----------------- Multiple Functions Demonstrating Scope ----------------- #
# Global variable
a = 1

# Function using global variable
def use_global():
    """Function using a global variable"""
    print("Inside use_global():", a)

# Function defining a local variable with the same name
def define_local():
    """Function with a local variable having the same name as global"""
    a = 2  # Local variable
    print("Inside define_local():", a)

# Function modifying a global variable
def modify_global_variable():
    """Function modifying global variable using 'global' keyword"""
    global a
    a = 3
    print("Inside modify_global_variable():", a)

# Global Scope Output
print("Global Scope Before Calling Functions:", a)

# Calling Functions
use_global()
print("Global Scope After use_global():", a)

define_local()
print("Global Scope After define_local():", a)

modify_global_variable()
print("Global Scope After modify_global_variable():", a)

