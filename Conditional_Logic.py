# Python If...Else Statements

# 1. Basic If Statement
print("1. BASIC IF STATEMENT")
a = 33
b = 200

if b > a:
    print("b is greater than a")

# 2. Indentation Example (Incorrect Indentation will raise an error)
# Uncommenting the below code will cause an error
# if b > a:
# print("b is greater than a")  # Incorrect indentation

# 3. Elif Statement
print("\n2. ELIF STATEMENT")
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# 4. Else Statement
print("\n3. ELSE STATEMENT")
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# 5. Short-Hand If
print("\n4. SHORT-HAND IF")
a = 50
b = 10

if a > b: print("a is greater than b")  # One-line if statement

# 6. Short-Hand If...Else (Ternary Operator)
print("\n5. SHORT-HAND IF...ELSE (TERNARY OPERATOR)")
a = 2
b = 330

print("A") if a > b else print("B")  # One-line if-else statement

# 7. Multiple Conditions in Short-Hand If...Else
print("\n6. MULTIPLE CONDITIONS IN SHORT-HAND IF...ELSE")
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")  # Multiple conditions in one line

# 8. AND Operator
print("\n7. AND OPERATOR")
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# 9. OR Operator
print("\n8. OR OPERATOR")
if a > b or a > c:
    print("At least one of the conditions is True")

# 10. NOT Operator
print("\n9. NOT OPERATOR")
a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")

# 11. Nested If Statements
print("\n10. NESTED IF STATEMENTS")
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# 12. The Pass Statement (Placeholder for Future Code)
print("\n11. PASS STATEMENT")

a = 33
b = 200

if b > a:
    pass  # Placeholder to avoid an error

print("Pass statement executed.")

