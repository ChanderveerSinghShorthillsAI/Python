# Demonstrating Precedence of Operators
expr = 10 + 20 * 30  # '*' has higher precedence than '+'
print("10 + 20 * 30 =", expr)  # Output: 610

# Logical Operators Precedence
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")  # Output: Hello! Welcome.
else:
    print("Good Bye!!")

# Using parentheses to change precedence
if (name == "Alex" or name == "John") and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")  # Output: Good Bye!!

# Demonstrating Associativity of Operators
# Left-to-right associativity
print("100 / 10 * 10 =", 100 / 10 * 10)  # Output: 100.0
print("5 - 2 + 3 =", 5 - 2 + 3)  # Output: 6
print("5 - (2 + 3) =", 5 - (2 + 3))  # Output: 0

# Right-to-left associativity
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)  # Output: 512 (2 ** (3 ** 2))

# Complex expression with precedence & associativity
expression = 100 + 200 / 10 - 3 * 10
print("100 + 200 / 10 - 3 * 10 =", expression)  # Output: 90.0