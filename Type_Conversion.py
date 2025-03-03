# Type Conversion in Python

# Implicit Type Conversion (Automatic by Python)
x = 10
print("x is of type:", type(x))

y = 10.6
print("y is of type:", type(y))

z = x + y  # int + float → float
print("Result of x + y:", z)
print("z is of type:", type(z))


# Explicit Type Conversion (Type Casting)
s = "10010"

# String to integer (base 2)
c = int(s, 2)
print("After converting to integer base 2:", c)

# String to float
e = float(s)
print("After converting to float:", e)



#  Type conversion using ord(), hex(), oct()
char = '4'
print("After converting character to integer:", ord(char))  # ASCII value

num = 56
print("After converting 56 to hexadecimal string:", hex(num))  # Hexadecimal
print("After converting 56 to octal string:", oct(num))  # Octal

# Type conversion using tuple(), set(), list()
s = 'geeks'

# String to tuple
print("After converting string to tuple:", tuple(s))

# String to set
print("After converting string to set:", set(s))

# String to list
print("After converting string to list:", list(s))



# Type conversion using dict(), complex(), str()
a = 1
b = 2

# Converting integers to complex numbers
print("After converting integer to complex number:", complex(a, b))

# Integer to string
print("After converting integer to string:", str(a))

# Tuple to dictionary
tup = (('a', 1), ('f', 2), ('g', 3))
print("After converting tuple to dictionary:", dict(tup))




print("ASCII 76 to character:", chr(76))
print("ASCII 77 to character:", chr(77))