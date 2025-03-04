# Python For Loops Demonstration

# Iterating through a list
print("Iterating through a list:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Iterating through a string
print("\nIterating through a string:")
for x in "banana":
    print(x)

# Using break statement
print("\nUsing break statement:")
for x in fruits:
    print(x)
    if x == "banana":
        break  # Stops the loop when "banana" is encountered

# Using break before print
print("\nUsing break before print:")
for x in fruits:
    if x == "banana":
        break
    print(x)

# Using continue statement
print("\nUsing continue statement:")
for x in fruits:
    if x == "banana":
        continue  # Skips "banana" and moves to the next iteration
    print(x)

# Using range() function
print("\nUsing range() function:")
for x in range(6):  # Iterates from 0 to 5
    print(x)

# Using range() with start parameter
print("\nUsing range() with start parameter:")
for x in range(2, 6):  # Iterates from 2 to 5
    print(x)

# Using range() with step parameter
print("\nUsing range() with step parameter:")
for x in range(2, 30, 3):  # Iterates from 2 to 29 with step 3
    print(x)

# Using else in for loop
print("\nUsing else in for loop:")
for x in range(6):
    print(x)
else:
    print("Loop finished!")

# Using else with break
print("\nUsing else with break:")
for x in range(6):
    if x == 3:
        break  # Stops execution before completing
    print(x)
else:
    print("Loop finished!")  # This won't execute since loop was broken

# Nested Loops
print("\nUsing Nested Loops:")
adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y)

# Using pass statement
print("\nUsing pass statement:")
for x in [0, 1, 2]:
    pass  # Does nothing but prevents an error

