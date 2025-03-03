# Creating a List
thislist = ["apple", "banana", "cherry"]
print(thislist)  # Output: ['apple', 'banana', 'cherry']

# Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # Output: 3

# List Items - Different Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types
mixed_list = ["abc", 34, True, 40, "male"]
print(mixed_list)  # Output: ['abc', 34, True, 40, 'male']

# Checking the type of a list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # Output: <class 'list'>

# Creating a list using the list() constructor
thislist = list(("apple", "banana", "cherry"))  # Note the double round brackets
print(thislist)  # Output: ['apple', 'banana', 'cherry']
