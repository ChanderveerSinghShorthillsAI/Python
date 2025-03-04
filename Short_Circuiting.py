# Short-Circuiting in Python

# 1. Short-Circuiting with `and` and `or`
print("1. SHORT-CIRCUITING WITH `and` AND `or`")

# Helper function to observe short-circuiting behavior
def check():
    print("geeks")
    return "geeks"

# `and` operator short-circuits if first value is False
print(1 and check())  # Output: "geeks"

# `or` operator short-circuits if first value is True
print(1 or check())  # Output: 1 (does not call check())

# `or` evaluates until it finds a truthy value
print(0 or check() or 1)  # Output: "geeks"

# `and` ensures all conditions are checked
print(0 or check() and 1)  # Output: "geeks", 1


# 2. Short-Circuiting in `all()` and `any()`
print("\n2. SHORT-CIRCUITING WITH `all()` AND `any()`")

def check(i):
    print("geeks")
    return i

# `all()` short-circuits on first False value
print(all(check(i) for i in [1, 1, 0, 0, 3]))  # Output: False

print("\r")

# `any()` short-circuits on first True value
print(any(check(i) for i in [0, 0, 0, 1, 3]))  # Output: True


# 3. Short-Circuiting in Conditional Operators
print("\n3. SHORT-CIRCUITING WITH CONDITIONAL OPERATORS")

def check(i):
    print("geeks")
    return i

# Stops evaluation as `10 > 11` is False
print(10 > 11 > check(3))  # Output: False

print("\r")

# Proceeds to evaluate `check(3)` as `10 < 11` is True
print(10 < 11 > check(3))  # Output: "geeks", True

print("\r")

# Evaluates `check(12)`, returning False
print(10 < 11 > check(12))  # Output: "geeks", False


# 4. Short-Circuiting in If-Elif Ladder
print("\n4. SHORT-CIRCUITING IN IF-ELIF LADDER")

a, b, c = 10, 20, 30

def printreturn(l):
    print(l)
    return l

if a == 11:
    print("a == 11")
elif b == 20 and c == 30:  # This is True
    print("b == 20 and c == 30")
elif b == a + a and 0 < len(printreturn("This was evaluated")):
    # Though True, this is not even evaluated
    print("b == a + a")

# Output: "b == 20 and c == 30"
