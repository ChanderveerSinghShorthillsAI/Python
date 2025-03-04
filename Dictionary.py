# Creating a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Dictionary:", thisdict)

# Accessing dictionary items
print("Brand:", thisdict["brand"])
print("Model using get():", thisdict.get("model"))

# Duplicate keys (latest value will overwrite)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020  # Overwrites previous year
}
print("Dictionary after duplicate key:", thisdict)

# Length of dictionary
print("Length of dictionary:", len(thisdict))

# Different data types in dictionary
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print("Dictionary with multiple data types:", thisdict)

# Type of dictionary
print("Type of dictionary:", type(thisdict))

# Using dict() constructor
newdict = dict(name="John", age=36, country="Norway")
print("Dictionary using dict():", newdict)

# Getting dictionary keys
x = thisdict.keys()
print("Keys before change:", x)
thisdict["engine"] = "V8"
print("Keys after adding 'engine':", x)

# Getting dictionary values
y = thisdict.values()
print("Values before change:", y)
thisdict["year"] = 2021
print("Values after changing 'year':", y)

# Getting dictionary items (key-value pairs)
z = thisdict.items()
print("Items before change:", z)
thisdict["color"] = "blue"
print("Items after adding 'color':", z)

# Checking if a key exists
if "model" in thisdict:
    print("Yes, 'model' is a key in the dictionary")

# Dictionary methods
copy_dict = thisdict.copy()  # Copy dictionary
thisdict.pop("year")  # Remove specific key
thisdict.popitem()  # Remove last key-value pair
thisdict.update({"dsdsdsd": 2025})  # Update dictionary
print("hello " , thisdict);
default_val = thisdict.setdefault("mileage", 15)  # Set default value
print("Updated dictionary:", thisdict)

# Clearing the dictionary
thisdict.clear()
print("Dictionary after clearing:", thisdict)
