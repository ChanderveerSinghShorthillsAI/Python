# Example: Get items from index 1 to 4 (excluding index 4)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])  # Output: [2, 3, 4]

# Get all elements in the list
print(a[::])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:])   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to the end
print(a[2:])  # Output: [3, 4, 5, 6, 7, 8, 9]

# Get elements from start to index 3 (excluding index 3)
print(a[:3])  # Output: [1, 2, 3]

# Get elements at specified intervals
print(a[::2])     # Output: [1, 3, 5, 7, 9]  (every second element)
print(a[1:8:3])   # Output: [2, 5, 8] (every third element from index 1 to 8)

# Out-of-bound slicing (No error, just returns available elements)
print(a[7:15])    # Output: [8, 9] (since list ends at index 8)

# Negative Indexing
print(a[-2:])     # Output: [8, 9] (last two elements)
print(a[:-3])     # Output: [1, 2, 3, 4, 5, 6] (all except last three)
print(a[-4:-1])   # Output: [6, 7, 8] (excluding -1 index)
print(a[-8:-1:2]) # Output: [2, 4, 6, 8] (every 2nd element from index -8 to -1)

# Reverse a list using slicing
print(a[::-1])    # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
