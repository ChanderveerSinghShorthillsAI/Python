# Example of Python Sets
s = {10, 50, 20}
print(s)
print(type(s))

# Type Casting with Python Set method
# Typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# Check unique and Immutable with Python Set
# A set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# This line will throw an error since set elements cannot be changed directly
# s[1] = "Hello"
# print(s)  # Uncomment to see the error

# Heterogeneous Element with Python Set
s = {"Geeks", "for", 10, 52.7, True}
print(s)

# Python Frozen Sets
# Normal Set
s = set(["a", "b", "c"])
print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])
print("\nFrozen Set")
print(fs)

# Uncommenting below line would cause an error as we are trying to add element to a frozen set
# fs.add("h")

# Adding elements to Python Sets
people = {"Jay", "Idrish", "Archi"}
print("People:", people)

# Adding an element
people.add("Daxit")

# Adding multiple elements using a loop
for i in range(1, 6):
    people.add(i)

print("\nSet after adding elements:", people)

# Union operation on Python Sets
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Using union() function
population = people.union(vampires)
print("Union using union() function")
print(population)

# Using "|" operator
population = people | dracula
print("\nUnion using '|' operator")
print(population)

# Intersection operation on Python Sets
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

# Using intersection() function
set3 = set1.intersection(set2)
print("Intersection using intersection() function")
print(set3)

# Using "&" operator
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)

# Finding Differences of Sets in Python
# Using difference() function
set3 = set1.difference(set2)
print("Difference of two sets using difference() function")
print(set3)

# Using '-' operator
set3 = set1 - set2
print("\nDifference of two sets using '-' operator")
print(set3)

# Clearing Python Sets
set1 = {1, 2, 3, 4, 5, 6}
print("Initial set")
print(set1)

# Clearing the set
set1.clear()
print("\nSet after using clear() function")
print(set1)
