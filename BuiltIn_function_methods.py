
# Demonstrating Python Built-in Functions with Examples

print(" Python Built-in Functions Demonstration\n")

# 1. abs() - Absolute value of a number
print("abs(-10):", abs(-10))

# 2. all() - Returns True if all elements in an iterable are True
print("all([True, 1, 'hello']):", all([True, 1, 'hello']))
print("all([True, 0, 'hello']):", all([True, 0, 'hello']))

# 3. any() - Returns True if any element in an iterable is True
print("any([False, 0, '']):", any([False, 0, '']))
print("any([False, 1, '']):", any([False, 1, '']))

# 4. bin() - Binary representation of a number
print("bin(10):", bin(10))

# 5. bool() - Boolean value of an object
print("bool([]):", bool([]))
print("bool([1, 2, 3]):", bool([1, 2, 3]))

# 6. bytearray() - Create a mutable bytes array
print("bytearray('hello', 'utf-8'):", bytearray("hello", "utf-8"))

# 7. bytes() - Immutable sequence of bytes
print("bytes('hello', 'utf-8'):", bytes("hello", "utf-8"))

# 8. callable() - Check if an object is callable
def my_func():
    pass
print("callable(my_func):", callable(my_func))
print("callable(10):", callable(10))

# 9. chr() - Convert Unicode code to character
print("chr(97):", chr(97))

# 10. complex() - Create a complex number
print("complex(3, 4):", complex(3, 4))

# 11. dict() - Create a dictionary
print("dict(a=1, b=2):", dict(a=1, b=2))

# 12. dir() - List attributes of an object
print("dir([]):", dir([])[:5])  # Displaying first 5 attributes for brevity

# 13. divmod() - Get quotient and remainder
print("divmod(10, 3):", divmod(10, 3))

# 14. enumerate() - Enumerate elements with an index
print("list(enumerate(['a', 'b', 'c'])):", list(enumerate(['a', 'b', 'c'])))

# 15. eval() - Evaluate a Python expression
print("eval('3 + 4'):", eval("3 + 4"))

# 16. filter() - Filter elements from an iterable
print("list(filter(lambda x: x > 2, [1, 2, 3, 4])):", list(filter(lambda x: x > 2, [1, 2, 3, 4])))

# 17. float() - Convert to float
print("float(5):", float(5))

# 18. format() - Format values
print("format(255, 'x'):", format(255, 'x'))  # Hexadecimal

# 19. frozenset() - Immutable set
print("frozenset([1, 2, 3]):", frozenset([1, 2, 3]))

# 20. getattr() - Get attribute value
class Test:
    x = 10
obj = Test()
print("getattr(obj, 'x'):", getattr(obj, 'x'))

# 21. globals() - Get global variables dictionary
print("globals()['__name__']:", globals()['__name__'])

# 22. hasattr() - Check if object has an attribute
print("hasattr(obj, 'x'):", hasattr(obj, 'x'))

# 23. hash() - Get hash value
print("hash('hello'):", hash('hello'))

# 24. help() - Get help documentation
# Uncomment below to see help output
# help(str)

# 25. hex() - Convert to hexadecimal
print("hex(255):", hex(255))

# 26. id() - Get object’s unique ID
print("id(obj):", id(obj))

# 27. input() - Get user input (Commented out for automation)
# name = input("Enter your name: ")
# print("Your name is", name)

# 28. int() - Convert to integer
print("int(3.7):", int(3.7))

# 29. isinstance() - Check if an object is an instance of a class
print("isinstance(10, int):", isinstance(10, int))

# 30. iter() - Create an iterator
it = iter([1, 2, 3])
print("next(it):", next(it))

# 31. len() - Get length of an object
print("len('hello'):", len('hello'))

# 32. list() - Create a list
print("list((1, 2, 3)):", list((1, 2, 3)))

# 33. map() - Apply function to an iterable
print("list(map(lambda x: x * 2, [1, 2, 3])):", list(map(lambda x: x * 2, [1, 2, 3])))

# 34. max() - Get max value
print("max([1, 5, 3]):", max([1, 5, 3]))

# 35. min() - Get min value
print("min([1, 5, 3]):", min([1, 5, 3]))

# 36. next() - Get next item from iterator
print("next(it):", next(it))

# 37. object() - Create new object
print("object():", object())

# 38. oct() - Convert to octal
print("oct(10):", oct(10))

# 39. open() - Open a file (commented for safety)
# f = open("test.txt", "w")
# f.write("Hello, world!")
# f.close()

# 40. ord() - Get Unicode code of a character
print("ord('A'):", ord('A'))

# 41. pow() - Get power of a number
print("pow(2, 3):", pow(2, 3))

# 42. print() - Print output
print("Hello, World!")

# 43. range() - Create a sequence
print("list(range(5)):", list(range(5)))

# 44. reversed() - Reverse an iterable
print("list(reversed([1, 2, 3])):", list(reversed([1, 2, 3])))

# 45. round() - Round a number
print("round(3.456, 2):", round(3.456, 2))

# 46. set() - Create a set
print("set([1, 2, 3]):", set([1, 2, 3]))

# 47. sorted() - Sort an iterable
print("sorted([3, 1, 2]):", sorted([3, 1, 2]))

# 48. str() - Convert to string
print("str(100):", str(100))

# 49. sum() - Sum of elements
print("sum([1, 2, 3]):", sum([1, 2, 3]))

# 50. tuple() - Convert to tuple
print("tuple([1, 2, 3]):", tuple([1, 2, 3]))

# 51. type() - Get object type
print("type(10):", type(10))

# 52. zip() - Zip multiple iterables
print("list(zip([1, 2], ['a', 'b'])):", list(zip([1, 2], ['a', 'b'])))


