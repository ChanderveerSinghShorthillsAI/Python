# Python Return Statement - A Complete Guide

# 1. Function Returning a Single Value
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def is_true(a):
    """Returns the boolean value of a."""
    return bool(a)

# Function Calls
res1 = add(2, 3)
print(res1)  # Output: 5

res2 = is_true(2 < 5)
print(res2)  # Output: True


# 2. Function Returning Multiple Values
def fun():
    """Returns multiple values as a tuple."""
    name = "Alice"
    age = 30
    return name, age

# Unpacking returned values
name, age = fun()
print(name)  # Output: Alice
print(age)   # Output: 30


# 3. Function Returning a List
def fun_list(n):
    """Returns a list containing the square and cube of n."""
    return [n**2, n**3]

# Function Call
res_list = fun_list(3)
print(res_list)  # Output: [9, 27]


# 4. Function Returning a Dictionary
def fun_dict(n):
    """Returns a dictionary with square and cube of n."""
    return {"square": n**2, "cube": n**3}

# Function Call
res_dict = fun_dict(3)
print(res_dict)  # Output: {'square': 9, 'cube': 27}


# 5. Function Returning Another Function
def fun1(msg):
    """Returns an inner function that uses msg."""
    def fun2():
        return f"Message: {msg}"
    return fun2  # Returning inner function

# Getting the inner function
fun3 = fun1("Hello, World!")

# Calling the inner function
print(fun3())  # Output: Message: Hello, World!


# 6. Function with Early Return
def check_even(n):
    """Checks if n is even and returns immediately."""
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(check_even(4))  # Output: Even
print(check_even(5))  # Output: Odd


# 7. Function with No Return (Implicitly Returns None)
def greet():
    """Prints a greeting message."""
    print("Hello!")

res_none = greet()  # This function doesn't return anything
print(res_none)  # Output: None


# 8. Returning a Lambda Function
def get_multiplier(factor):
    """Returns a lambda function that multiplies by factor."""
    return lambda x: x * factor

double = get_multiplier(2)
print(double(5))  # Output: 10
