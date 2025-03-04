# Python While Loop Demonstration

# Example 1: Basic while loop
print("Example 1: Basic while loop")
i = 1
while i < 6:
    print(i)
    i += 1

# Example 2: Using break to exit the loop when i reaches 3
print("\nExample 2: Using break statement")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # Exit loop when i == 3
    i += 1

# Example 3: Using continue to skip iteration when i is 3
print("\nExample 3: Using continue statement")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skip printing when i == 3
    print(i)

# Example 4: Using else with while loop
print("\nExample 4: Using else statement with while loop")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Example 5: Infinite loop demonstration (Warning: Do not run without exit condition!)
# Uncomment to test, but ensure you have an exit condition
# print("\nExample 5: Infinite loop (Use with caution!)")
# i = 1
# while True:
#     print(i)
#     if i == 10:
#         break  # Exit after 10 iterations
#     i += 1

# Example 6: Looping with user input
print("\nExample 6: Looping with user input")
count = 0
while count < 3:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    count += 1

# Example 7: Decrementing while loop
print("\nExample 7: Decrementing while loop")
i = 5
while i > 0:
    print(i)
    i -= 1

# Example 8: Nested while loops
print("\nExample 8: Nested while loops")
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
