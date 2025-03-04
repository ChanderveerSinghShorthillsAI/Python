# Basic List Unpacking
colors = ['red', 'blue', 'green']

# Unpacking the list into separate variables
red, blue, green = colors

print("red:", red)     # Output: red
print("blue:", blue)   # Output: blue
print("green:", green) # Output: green

# Incorrect Unpacking - This will raise an error
# red, blue = colors  # ValueError: too many values to unpack (expected 2)

# Unpacking with an asterisk (*) to handle extra elements
colors = ['red', 'blue', 'green']
red, blue, *other = colors

print("\nUnpacking with *:")
print("red:", red)     # Output: red
print("blue:", blue)   # Output: blue
print("other:", other) # Output: ['green']

# Another example with more elements
colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors

print("\nAnother unpacking example:")
print("cyan:", cyan)       # Output: cyan
print("magenta:", magenta) # Output: magenta
print("other:", other)     # Output: ['yellow', 'black']
