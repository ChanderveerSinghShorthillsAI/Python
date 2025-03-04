# Ternary Operator in Python

# 1. Basic Example: Check if a number is Even or Odd
print("1. BASIC TERNARY OPERATOR")
n = 5
res = "Even" if n % 2 == 0 else "Odd"
print(res)  # Output: Odd

# 2. Ternary Operator in Nested If-Else
print("\n2. TERNARY OPERATOR IN NESTED IF-ELSE")
n = -5
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)  # Output: Negative

# 3. Ternary Operator using Tuple Indexing
print("\n3. TERNARY OPERATOR USING TUPLE")
n = 7
res = ("Odd", "Even")[n % 2 == 0]  # Condition acts as index (0 or 1)
print(res)  # Output: Odd

# 4. Ternary Operator using Dictionary
print("\n4. TERNARY OPERATOR USING DICTIONARY")
a, b = 10, 20
max_value = {True: a, False: b}[a > b]  # True selects a, False selects b
print(max_value)  # Output: 20

# 5. Ternary Operator using Lambda
print("\n5. TERNARY OPERATOR USING LAMBDA")
max_value = (lambda x, y: x if x > y else y)(a, b)
print(max_value)  # Output: 20

# 6. Ternary Operator with Print Function
print("\n6. TERNARY OPERATOR WITH PRINT FUNCTION")
print("a is greater" if a > b else "b is greater")  # Output: b is greater

