# Difference Between Methods and Functions in Python

# 1. Python Method (Defined within a Class)
class ABC:
    """A simple class with a method."""
    
    def method_abc(self):
        """This is a method associated with an instance of a class."""
        print("I am in method_abc of ABC class.")

# Creating an object of ABC class
class_ref = ABC()

# Calling the method using the object
class_ref.method_abc()

# Output:
# I am in method_abc of ABC class


# 2. Python Inbuilt Method (Method from a module)
import math

# Using math.ceil() method from the math module
ceil_val = math.ceil(15.25)
print("Ceiling value of 15.25 is:", ceil_val)

# Output:
# Ceiling value of 15.25 is: 16


# 3. Python Function (Independent function)
def subtract(a, b):
    """This is an independent function, not inside a class."""
    return a - b

# Calling the function
print(subtract(10, 12))  # Output: -2
print(subtract(15, 6))   # Output: 9


# 4. Python Inbuilt Function (Built-in Python function)
s = sum([5, 15, 2])  # sum() function
print(s)  # Output: 22

mx = max(15, 6)  # max() function
print(mx)  # Output: 15


# 5. Difference Between Function and Method
class Demo:
    """Class to show difference between method and function."""
    
    def class_method(self):
        """This is a method and needs an instance to call."""
        print("This is a method inside a class.")

# Function
def standalone_function():
    """This is a standalone function, not bound to a class."""
    print("This is a standalone function.")

# Creating an instance of Demo class
obj = Demo()

# Calling the method using the instance
obj.class_method()

# Calling the function independently
standalone_function()

# Output:
# This is a method inside a class.
# This is a standalone function.
