# append(): Adds an element to the end of the list.
a = [1, 2, 3]
a.append(4)
print("append():", a)  # Output: [1, 2, 3, 4]

# copy(): Returns a shallow copy of the list.
b = a.copy()
print("copy():", b)  # Output: [1, 2, 3, 4]

# clear(): Removes all elements from the list.
a.clear()
print("clear():", a)  # Output: []

# count(): Returns the number of times a specified element appears in the list.
a = [1, 2, 3, 2]
print("count(2):", a.count(2))  # Output: 2

# extend(): Adds elements from another list to the end of the current list.
a = [1, 2]
a.extend([3, 4])
print("extend():", a)  # Output: [1, 2, 3, 4]

# index(): Returns the index of the first occurrence of a specified element.
a = [1, 2, 3]
print("index(2):", a.index(2))  # Output: 1

# insert(): Inserts an element at a specified position.
a = [1, 3]
a.insert(1, 2)
print("insert():", a)  # Output: [1, 2, 3]

# pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
a = [1, 2, 3]
a.pop()
print("pop():", a)  # Output: [1, 2]

# remove(): Removes the first occurrence of a specified element.
a = [1, 2, 3]
a.remove(2)
print("remove():", a)  # Output: [1, 3]

# reverse(): Reverses the order of the elements in the list.
a = [1, 2, 3]
a.reverse()
print("reverse():", a)  # Output: [3, 2, 1]

# sort(): Sorts the list in ascending order.
a = [3, 1, 2]
a.sort()
print("sort():", a)  # Output: [1, 2, 3]
