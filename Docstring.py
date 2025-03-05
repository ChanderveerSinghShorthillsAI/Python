# 1. **Single-line Docstring**
def greet():
    """This function prints a greeting message."""
    print("Hello, welcome to Python!")

# Accessing the docstring
print(greet.__doc__)

# Calling the function
greet()


# 2. **Multi-line Docstring**
def add_numbers(a, b):
    """
    This function takes two numbers as input.
    It returns the sum of the two numbers.
    
    Parameters:
    a (int or float): The first number
    b (int or float): The second number
    
    Returns:
    int or float: The sum of a and b
    """
    return a + b

# Accessing the multi-line docstring
print(add_numbers.__doc__)

# Calling the function
print(add_numbers(3, 5))


# 3. **Class Docstring**
class Animal:
    """
    This is an Animal class.
    
    Attributes:
    name (str): The name of the animal
    species (str): The species of the animal
    """
    
    def __init__(self, name, species):
        """Constructor method to initialize attributes."""
        self.name = name
        self.species = species

    def make_sound(self, sound):
        """This method prints the sound the animal makes."""
        print(f"{self.name} says {sound}")

# Accessing class docstring
print(Animal.__doc__)

# Creating an object of Animal class
dog = Animal("Dog", "Mammal")

# Accessing method docstring
print(dog.make_sound.__doc__)

# Calling the method
dog.make_sound("Woof!")


# 4. **Module-Level Docstring**
"""
This module demonstrates different types of docstrings in Python.

It includes:
- Single-line docstrings
- Multi-line docstrings
- Class docstrings
- Method docstrings
- Module-level docstrings
"""



# 6. **Accessing Docstrings Using help() Function**
help(Animal)
help(add_numbers)
help(greet)
