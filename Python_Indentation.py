# Python Indentation

# 1. Correct Indentation
print("1. CORRECT INDENTATION")

if 5 > 2:
    print("Five is greater than two!")  # Properly indented block

# 2. Incorrect Indentation (This will cause a SyntaxError if uncommented)
# print("\n2. INCORRECT INDENTATION")
# if 5 > 2:
# print("Five is greater than two!")  # Incorrect indentation (missing spaces)
# Uncomment the above code to see the indentation error.

# 3. Different Levels of Indentation (Valid)
print("\n3. DIFFERENT LEVELS OF INDENTATION")

if 5 > 2:
 print("Five is greater than two!")  # 1 space indentation (Valid)

if 5 > 2:
        print("Five is greater than two!")  # 8 spaces indentation (Valid)

# 4. Inconsistent Indentation (This will cause an error if uncommented)
# print("\n4. INCONSISTENT INDENTATION")
# if 5 > 2:
#     print("Five is greater than two!")  # 4 spaces
#        print("Five is greater than two!")  # 8 spaces (Invalid)
# Uncomment the above code to see the indentation error.

# 5. Indentation in Loops and Functions
print("\n5. INDENTATION IN LOOPS AND FUNCTIONS")

# Indentation in loops
for i in range(3):
    print("Loop iteration:", i)  # Proper indentation inside the loop

# Indentation in functions
def greet():
    print("Hello, world!")  # Proper indentation inside function

greet()

# 6. Indentation in Nested Blocks
print("\n6. INDENTATION IN NESTED BLOCKS")

if 10 > 5:
    print("Outer condition is True")
    if 10 > 8:
        print("Inner condition is also True")  # Nested indentation


