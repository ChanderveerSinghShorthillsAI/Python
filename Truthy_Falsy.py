# Truthy vs Falsy Values in Python

# 1. Example of a Truthy Value
print("1. TRUTHY VALUE CHECK")

number = 7  # Non-zero numbers are truthy
if number:
    print(f"{number} is a truthy value")

# 2. Example of a Falsy Value
print("\n2. FALSY VALUE CHECK")

number = 0  # Zero is falsy
if number:
    print(f"{number} is a truthy value")  # This won't execute
else:
    print(f"{number} is a falsy value")

# 3. List of Falsy Values
print("\n3. LIST OF FALSY VALUES")

falsy_values = [[], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False]

for value in falsy_values:
    print(f"{repr(value)} -> {bool(value)}")  # All should return False

# 4. List of Truthy Values
print("\n4. LIST OF TRUTHY VALUES")

truthy_values = [[1, 2], (3, 4), {"a": 1}, {5, 6}, "Hello", range(1), 42, -5, 0.1, True]

for value in truthy_values:
    print(f"{repr(value)} -> {bool(value)}")  # All should return True

# 5. Using the bool() Function
print("\n5. USING THE bool() FUNCTION")

print(bool(7))     # True
print(bool(0))     # False
print(bool([]))    # False
print(bool({7, 4}))  # True
print(bool(-4))    # True
print(bool(0.0))   # False
print(bool(None))  # False
print(bool(1))     # True
print(bool(range(0)))  # False
print(bool(set()))  # False
print(bool([1, 2, 3, 4]))  # True

# 6. Truthy and Falsy Values in a Function
print("\n6. FUNCTION DEMONSTRATING TRUTHY & FALSY VALUES")

def even_odd(number):
    if number % 2:  
        return 'Odd number'  # num % 2 == 1 is a truthy value
    else:  
        return 'Even number'  # num % 2 == 0 is a falsy value

# Checking numbers
print(even_odd(7))  # Odd number
print(even_odd(4))  # Even number
