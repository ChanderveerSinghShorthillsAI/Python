class A:
    cnt = 0  # Class variable

    def __init__(self):
        A.cnt += 1  # Increment the class variable

    def getcnt(self):
        return A.cnt  # Access the class variable

a = A()
print(a.getcnt())  # Output: 1
b = A()
print(A.cnt)  # Output: 2
print(b.getcnt())  # Output: 2

        