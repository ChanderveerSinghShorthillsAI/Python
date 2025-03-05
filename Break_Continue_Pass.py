# Loop Control Statements in Python

# 1. Break Statement
print("Break Statement Example (For Loop):")
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

print("\nBreak Statement Example (While Loop):")
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    i += 1

# 2. Continue Statement
print("\nContinue Statement Example:")
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the code for i = 3
    print(i)

# 3. Pass Statement
print("\nPass Statement Example:")
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code, does nothing
    print(i)
