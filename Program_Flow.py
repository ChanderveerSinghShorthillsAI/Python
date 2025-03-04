

# 1. IF STATEMENTS
print("1. IF STATEMENTS")
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# 2. FOR LOOPS
print("\n2. FOR LOOPS")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() in a for loop
print("Numbers from 0 to 4 using range():")
for i in range(5):
    print(i)

# 3. WHILE LOOPS
print("\n3. WHILE LOOPS")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# 4. BREAK AND CONTINUE STATEMENTS
print("\n4. BREAK AND CONTINUE")

# Break example
for num in range(10):
    if num == 5:
        print("Breaking the loop at 5")
        break
    print(num)

# Continue example
print("Skipping number 5 using continue:")
for num in range(10):
    if num == 5:
        continue
    print(num)

# 5. FUNCTION DEFINITIONS
print("\n5. FUNCTION DEFINITIONS")

def greet(name):
    """A function to greet the user"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with default argument
def power(base, exponent=2):
    """Function to calculate power"""
    return base ** exponent

print("3 squared is:", power(3))
print("2 raised to 3 is:", power(2, 3))

# 6. MATCH CASE (Python 3.10+)
print("\n6. MATCH CASE")

def match_example(value):
    """Example of match case in Python 3.10+"""
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Unknown number"

print(match_example(1))
print(match_example(5))

# 7. PASS STATEMENT (Used as a placeholder)
print("\n7. PASS STATEMENT")

for _ in range(3):
    pass  # Does nothing, just a placeholder

def not_implemented():
    pass  # Placeholder for future function

print("Pass statement executed.")

# 8. USING ELSE WITH LOOPS
print("\n8. USING ELSE WITH LOOPS")

for num in range(3):
    print(num)
else:
    print("Loop completed without break.")

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed without break.")

# 9. FUNCTION WITH ARBITRARY ARGUMENTS
print("\n9. FUNCTION WITH ARBITRARY ARGUMENTS")

def sum_all(*numbers):
    """Function to sum all given numbers"""
    return sum(numbers)

print("Sum of numbers 1, 2, 3, 4:", sum_all(1, 2, 3, 4))

# 10. LAMBDA FUNCTIONS
print("\n10. LAMBDA FUNCTIONS")

square = lambda x: x * x
print("Square of 4:", square(4))

add = lambda x, y: x + y
print("Sum of 3 and 5:", add(3, 5))

# 11. FUNCTION WITH KEYWORD ARGUMENTS
print("\n11. FUNCTION WITH KEYWORD ARGUMENTS")

def person_details(name, age):
    """Function with keyword arguments"""
    return f"Name: {name}, Age: {age}"

print(person_details(age=30, name="Bob"))

# 12. FUNCTION RETURNING MULTIPLE VALUES
print("\n12. FUNCTION RETURNING MULTIPLE VALUES")

def get_coordinates():
    """Function returning multiple values as a tuple"""
    return (10, 20)

x, y = get_coordinates()
print("Coordinates:", x, y)

# 13. USING GLOBAL VARIABLES
print("\n13. USING GLOBAL VARIABLES")

global_var = "I am global"

def modify_global():
    global global_var
    global_var = "Modified global variable"

modify_global()
print(global_var)

# 14. FUNCTION WITH NESTED FUNCTIONS
print("\n14. FUNCTION WITH NESTED FUNCTIONS")

def outer_function(msg):
    """Function containing another function"""
    def inner_function():
        print("Inner function says:", msg)
    inner_function()

outer_function("Hello from inner function!")

# 15. DOCSTRINGS IN FUNCTIONS
print("\n15. DOCSTRINGS IN FUNCTIONS")

def example_function():
    """This is a function that serves as an example."""
    return "Docstrings can be accessed using __doc__."

print(example_function.__doc__)

