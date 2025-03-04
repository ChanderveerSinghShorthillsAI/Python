# Creating a Tuple
t = (10, 20, 30)
print(t)
print(type(t))

# Immutable nature of tuples
t = (1, 2, 3, 4, 5)
print(t[1])  # Accessing elements
print(t[4])

# Tuples can contain duplicate elements
t = (1, 2, 3, 4, 2, 3)
print(t)

# Attempting to update an element (will raise an error)
try:
    t[1] = 100
except TypeError as e:
    print(e)

# Accessing values using positive index
t = (10, 5, 20)
print("Value in t[0] =", t[0])
print("Value in t[1] =", t[1])
print("Value in t[2] =", t[2])

# Accessing values using negative index
print("Value in t[-1] =", t[-1])
print("Value in t[-2] =", t[-2])
print("Value in t[-3] =", t[-3])

# Traversing a tuple
t = (1, 2, 3, 4, 5)
for x in t:
    print(x, end=" ")
print()

# Concatenation of tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')
print(t1 + t2)

# Nesting tuples
t3 = (t1, t2)
print(t3)

# Repetition in tuples
t = ('python',) * 3
print(t)

# Slicing tuples
t = (0, 1, 2, 3)
print(t[1:])    # From index 1 to end
print(t[::-1])  # Reverse tuple
print(t[2:4])   # Elements from index 2 to 3

# Deleting a tuple (will raise an error if accessed after deletion)
t = (0, 1)
del t
try:
    print(t)
except NameError as e:
    print(e)

# Finding length of a tuple
t = ('python', 'geek')
print(len(t))

# Tuple with multiple data types
t = ("immutable", True, 23)
print(t)

# Converting a list to a tuple
a = [0, 1, 2]
t = tuple(a)
print(t)

# Creating tuples inside a loop
t = ('gfg',)
n = 5
for i in range(n):
    t = (t,)
    print(t)

# Different ways to create tuples
# Using round brackets
t = ("gfg", "Python") 
print(t)

# Using comma separated values
t = 4, 5, 6
print(t)

# Using tuple constructor
t = tuple([7, 8, 9])
print(t)

# Creating an empty tuple
t = ()
print(t)

# Single element tuple (with comma)
t = (10,)
print(t)
print(type(t))

# Without comma (not a tuple)
t = (10)
print(t)
print(type(t))

# Tuple packing
a, b, c = 11, 12, 13
t = (a, b, c)
print(t)
