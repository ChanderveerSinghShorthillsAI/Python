# Python range() Function Demonstration

# Example 1: Default range (start=0, step=1)
print("Range from 0 to 5:")
x = range(6)  # Generates numbers from 0 to 5
for n in x:
    print(n)

# Example 2: Specifying start and stop
print("\nRange from 3 to 5:")
x = range(3, 6)  # Generates numbers from 3 to 5
for n in x:
    print(n)

# Example 3: Specifying step value
print("\nRange from 3 to 19 with step 2:")
x = range(3, 20, 2)  # Generates numbers from 3 to 19, incrementing by 2
for n in x:
    print(n)

# Example 4: Using range() with a negative step
print("\nRange from 10 to 0 with step -2:")
x = range(10, 0, -2)  # Generates numbers from 10 to 1, decrementing by 2
for n in x:
    print(n)

# Example 5: Converting range to a list
print("\nConvert range to a list:")
numbers = list(range(1, 11))  # Generates a list of numbers from 1 to 10
print(numbers)

# Example 6: Using range() in a list comprehension
print("\nUsing range() in a list comprehension:")
squares = [n**2 for n in range(1, 6)]  # Generates squares of numbers from 1 to 5
print(squares)
