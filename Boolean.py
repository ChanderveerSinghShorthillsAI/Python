# Boolean Values - Comparing two values
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# Using Booleans in an if statement
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluating values using bool()
print(bool("Hello"))  # True
print(bool(15))       # True

# Evaluating variables using bool()
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True
