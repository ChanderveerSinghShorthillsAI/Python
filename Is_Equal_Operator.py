# Difference Between == and is Operator

# Creating two lists with the same values
x = [1, 2, 3]
y = [1, 2, 3]
z = x  # Assigning x to z (both now refer to the same object)

# Using the == operator (Equality Comparison)
print("Using == operator:")
if x == y:
    print("x == y: True")  # True because values are the same
else:
    print("x == y: False")

# Using the 'is' operator (Identity Comparison)
print("\nUsing 'is' operator:")
if x is y:
    print("x is y: True")  # False, because x and y are different objects in memory
else:
    print("x is y: False")

# Checking reference comparison with 'is'
if x is z:
    print("x is z: True")  # True, because z refers to the same object as x
else:
    print("x is z: False")