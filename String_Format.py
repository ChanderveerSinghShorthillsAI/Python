# Python String format() Method Demonstration

# Different placeholder values
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)

print("\nNamed, Numbered, and Empty Placeholders Example:")
print(txt1)  # My name is John, I'm 36
print(txt2)  # My name is John, I'm 36
print(txt3)  # My name is John, I'm 36

# Formatting types
num = 1234567.89

print("\nFormatting Types Example:")
print("Left aligned: {:<15}".format(num))       # Left align
print("Right aligned: {:>15}".format(num))      # Right align
print("Center aligned: {:^15}".format(num))     # Center align
print("Sign placement: {:=+15}".format(num))    # Sign at the leftmost position
print("Plus sign: {:+15}".format(num))          # Explicit + for positive numbers
print("Minus sign: {:-15}".format(-num))        # Minus for negative numbers
print("Space before positive: {: 15}".format(num))  # Space before positive numbers
print("Comma separator: {:,}".format(num))      # Thousand separator using comma
print("Underscore separator: {:_}".format(num)) # Thousand separator using underscore
print("Binary format: {:b}".format(255))        # Binary format
print("Unicode char: {:c}".format(65))          # Unicode character (A)
print("Decimal format: {:d}".format(255))       # Decimal format
print("Scientific (lowercase): {:e}".format(num)) # Scientific notation (lowercase)
print("Scientific (uppercase): {:E}".format(num)) # Scientific notation (uppercase)
print("Fixed point: {:.2f}".format(num))        # Fixed point format
print("Percentage: {:.2%}".format(0.75))        # Percentage format
print("Hex (lowercase): {:x}".format(255))      # Hexadecimal (lowercase)
print("Hex (uppercase): {:X}".format(255))      # Hexadecimal (uppercase)
