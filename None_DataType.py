# Assign None to a variable
x = None

# Print the value of x
print("Value of x:", x)  # Output: None

# Check the data type of None
print("Type of x:", type(x))  # Output: <class 'NoneType'>

# Boolean evaluation of None
if x:
    print("Do you think None is True?")
elif x is False:
    print("Do you think None is False?")
else:
    print("None is not True or False, None is just None...")  
    # Output: None is not True or False, None is just None...

# None is not equal to 0, False, or an empty string
print("\nNone == 0:", None == 0)        # Output: False
print("None == False:", None == False)  # Output: False
print("None == '':", None == '')        # Output: False

# A function that returns None by default
def example_function():
    pass  # No return statement, so it implicitly returns None

result = example_function()
print("\nFunction return value:", result)  # Output: None

# Checking if a variable is None
if result is None:
    print("The function returned None.")  # Output: The function returned None.
