# Python Strings

# Displaying a string
print("Hello")
print('Hello')

# Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assigning a string to a variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# Strings are arrays - Accessing elements
a = "Hello, World!"
print("Character at index 1:", a[1])  # 'e'

# Looping Through a String
for x in "banana":
    print(x, end=" ")  # Prints each letter of "banana" in a loop
print()  # New line

# String Length
print("Length of string:", len(a))

# Check if substring is present in a string
txt = "The best things in life are free!"
print("'free' in text:", "free" in txt)

# Using 'in' inside an if-statement
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if a substring is NOT in the string
print("'expensive' not in text:", "expensive" not in txt)

# Using 'not in' inside an if-statement
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
