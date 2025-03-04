# Python enumerate() Function Demonstration

# Example 1: Using enumerate() to iterate with an index
print("Using enumerate() with a list:")
a = ["Geeks", "for", "Geeks"]
for i, name in enumerate(a):
    print(f"Index {i}: {name}")

# Example 2: Converting enumerate object to a list of tuples
print("\nConverting enumerate object to a list:")
enumerate_list = list(enumerate(a))
print(enumerate_list)

# Example 3: Using enumerate() with a custom start index
print("\nUsing enumerate() with a custom start index (starting from 1):")
for index, value in enumerate(a, start=1):
    print(f"Index {index}: {value}")

# Example 4: Printing enumerate object directly
print("\nPrinting enumerate object directly:")
for ele in enumerate(a):
    print(ele)

# Example 5: Using next() function to get the next element from an enumerate object
print("\nUsing next() with enumerate object:")
b = enumerate(a)
print(b)  # Output: <enumerate object at 0x0000023D3D3D3D80>
print(next(b))  # Retrieves first element (index 0)
print(next(b))  # Retrieves second element (index 1)

# Example 6: Using a tuple unpacking in a loop
print("\nUsing tuple unpacking in a loop:")
for index, value in enumerate(["apple", "banana", "cherry"]):
    print(f"{index} -> {value}")

# Example 7: Using enumerate() with a tuple
print("\nUsing enumerate() with a tuple:")
my_tuple = ("Python", "Java", "C++")
for idx, val in enumerate(my_tuple):
    print(f"{idx}: {val}")

# Example 8: Using enumerate() with a dictionary (iterating over keys)
print("\nUsing enumerate() with a dictionary:")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for idx, key in enumerate(my_dict):
    print(f"{idx}: {key} -> {my_dict[key]}")

# Example 9: Using enumerate() with a set
print("\nUsing enumerate() with a set:")
my_set = {"apple", "banana", "cherry"}
for idx, val in enumerate(my_set):
    print(f"{idx}: {val}")

