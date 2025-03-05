"""
Scope Resolution in Python - LEGB Rule

LEGB Rule Hierarchy:
1. **Local (L)**   - Variables defined inside a function.
2. **Enclosed (E)** - Variables in enclosing functions (nested functions).
3. **Global (G)**  - Variables defined at the uppermost level of the script/module.
4. **Built-in (B)** - Names reserved in Python's built-in modules.

This script demonstrates:
✔ Local Scope
✔ Global Scope
✔ Enclosed Scope
✔ Built-in Scope
"""

# ----------------- Local Scope Example ----------------- #
def local_scope_example():
    """Demonstrates Local Scope"""
    pi = "Local pi variable"  # Local variable
    print("Inside Function:", pi)  # Access local variable

# Function call
local_scope_example()
# Uncommenting the following line will raise an error:
# print(pi)  # NameError: name 'pi' is not defined


# ----------------- Global Scope Example ----------------- #
pi = "Global pi variable"  # Global variable

def global_scope_example():
    """Demonstrates Global Scope"""
    print("Inside Function:", pi)  # Accessing global variable

# Function call
global_scope_example()
print("Outside Function:", pi)  # Accessing global variable outside function


# ----------------- Local & Global Scopes Example ----------------- #
def local_global_example():
    """Demonstrates Local and Global Scope"""
    pi = "Local pi variable"  # Local variable
    print("Inside Function:", pi)  # Local variable takes precedence

# Function call
local_global_example()
print("Outside Function:", pi)  # Accessing global variable


# ----------------- Enclosed Scope Example ----------------- #
def outer_function():
    """Demonstrates Enclosed Scope"""
    pi = "Outer pi variable"  # Enclosed variable

    def inner_function():
        nonlocal pi  # Refers to outer function's variable
        print("Inside Inner Function:", pi)  # Enclosed scope

    inner_function()

# Function call
outer_function()
print("Outside Function:", pi)  # Accessing global variable


# ----------------- Built-in Scope Example ----------------- #
from math import pi  # Importing pi from math module (Built-in Scope)

def built_in_scope_example():
    """Demonstrates Built-in Scope"""
    print("Built-in Scope pi:", pi)  # Uses the built-in `pi` from math module

# Function call
built_in_scope_example()

# Uncommenting the following line will show the built-in `pi`
# print(pi)  # Output: 3.141592653589793

