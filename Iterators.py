# Python Iterators Demonstration

# Example 1: Using iter() and next() with a tuple
print("Using iter() and next() with a tuple:")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # Output: apple
print(next(myit))  # Output: banana
print(next(myit))  # Output: cherry

# Example 2: Using iter() and next() with a string
print("\nUsing iter() and next() with a string:")
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # Output: b
print(next(myit))  # Output: a
print(next(myit))  # Output: n
print(next(myit))  # Output: a
print(next(myit))  # Output: n
print(next(myit))  # Output: a

# Example 3: Looping through a tuple using a for loop
print("\nLooping through a tuple using a for loop:")
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# Example 4: Looping through a string using a for loop
print("\nLooping through a string using a for loop:")
mystr = "banana"
for x in mystr:
    print(x)