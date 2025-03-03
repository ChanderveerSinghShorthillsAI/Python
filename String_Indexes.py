# String Indexing in Python
s = 'mybacon'

# Accessing characters using positive indexes
print("Positive Indexing:")
print("s[0]:", s[0])   # 'm'
print("s[1]:", s[1])   # 'y'
print("s[6]:", s[6])   # 'n'
print("s[len(s) - 1]:", s[len(s) - 1])  # 'n' (last character)



# Accessing characters using negative indexes
print("\nNegative Indexing:")
print("s[-1]:", s[-1])  # 'n'
print("s[-4]:", s[-4])  # 'a'
print("s[-len(s)]:", s[-len(s)])  # 'm'
print("s[-7]:", s[-7])  # 'm'



# Working with an empty string
t = ''
print("\nWorking with an empty string:")
print("Type of t:", type(t))  # <class 'str'>
print("Length of t:", len(t))  # 0

