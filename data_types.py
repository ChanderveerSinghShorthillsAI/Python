# Defining variables
x = "Hello World"
print(x, "->", type(x))

x = 20
print(x, "->", type(x))

x = 20.5
print(x, "->", type(x))

x = 1j
print(x, "->", type(x))

x = ["apple", "banana", "cherry"]
print(x, "->", type(x))

x = ("apple", "banana", "cherry")
print(x, "->", type(x))

x = range(6)
print(x, "->", type(x))

x = {"name": "John", "age": 36}
print(x, "->", type(x))

x = {"apple", "banana", "cherry"}
print(x, "->", type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x, "->", type(x))

x = True
print(x, "->", type(x))

x = b"Hello"
print(x, "->", type(x))

x = bytearray(5)
print(x, "->", type(x))

x = memoryview(bytes(5))
print(x, "->", type(x))

x = None
print(x, "->", type(x))


# Output:
# Hello World -> <class 'str'>
# 20 -> <class 'int'>
# 20.5 -> <class 'float'>
# 1j -> <class 'complex'>
# ['apple', 'banana', 'cherry'] -> <class 'list'>
# ('apple', 'banana', 'cherry') -> <class 'tuple'>
# range(0, 6) -> <class 'range'>
# {'name': 'John', 'age': 36} -> <class 'dict'>
# {'banana', 'cherry', 'apple'} -> <class 'set'>
# frozenset({'banana', 'cherry', 'apple'}) -> <class 'frozenset'>
# True -> <class 'bool'>
# b'Hello' -> <class 'bytes'>
# bytearray(b'\x00\x00\x00\x00\x00') -> <class 'bytearray'>
# <memory at 0x7f31326719c0> -> <class 'memoryview'>
# None -> <class 'NoneType'>