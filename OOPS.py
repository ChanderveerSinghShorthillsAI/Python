# Python Object-Oriented Programming (OOP) Concepts

# 1. Class and Objects
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating objects
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.display_info()
car2.display_info()

# 2. The __init__ Method (Constructor)
# The __init__ method initializes the object when it's created.

# 3. Self and Comparing Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age > other.age:
            print(f"{self.name} is older than {other.name}")
        else:
            print(f"{self.name} is younger than or the same age as {other.name}")

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

p1.compare_age(p2)

# 4. Types of Variables (Instance & Class Variables)
class Employee:
    company = "TechCorp"  # Class variable (shared across all instances)

    def __init__(self, name, salary):
        self.name = name        # Instance variable
        self.salary = salary

emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

print(Employee.company, emp1.name, emp1.salary)
print(emp2.company, emp2.name, emp2.salary)

# Changing class variable
Employee.company = "NewTech"

print(emp1.company, emp2.company)  # Both will reflect the change

# 5. Types of Methods (Instance, Class, and Static Methods)
class MathOperations:
    def __init__(self, num):
        self.num = num

    def square(self):  # Instance Method
        return self.num ** 2

    @classmethod
    def cube(cls, x):  # Class Method
        return x ** 3

    @staticmethod
    def add(a, b):  # Static Method
        return a + b

math_obj = MathOperations(5)
print(math_obj.square())
print(MathOperations.cube(3))
print(MathOperations.add(10, 20))

# 6. Inner Class
class Outer:
    class Inner:
        def __init__(self):
            print("Inner class object created")

    def __init__(self):
        print("Outer class object created")
        self.inner_obj = self.Inner()

outer_obj = Outer()

# 7. Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def display(self):
        print(f"Child class inheriting from Parent: {self.name}")

child_obj = Child("ParentName")
child_obj.show()
child_obj.display()

# 8. Constructor in Inheritance
class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal {species} created")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")  # Calls parent constructor
        self.breed = breed
        print(f"Dog breed: {breed}")

dog_obj = Dog("Labrador")

# 9. Multiple Inheritance
class Father:
    def trait_father(self):
        print("Father's Trait: Hardworking")

class Mother:
    def trait_mother(self):
        print("Mother's Trait: Kindness")

class Child(Father, Mother):  # Inheriting from both Father and Mother
    def traits(self):
        print("Child inherits traits from both parents.")

child = Child()
child.trait_father()
child.trait_mother()
child.traits()

# 10. Multilevel Inheritance
class Grandparent:
    def __init__(self):
        print("Grandparent Constructor Called")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent Constructor Called")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor Called")

child_obj = Child()  # Will call constructors from all levels

# 11. Polymorphism
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

def animal_speak(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()

animal_speak(cat)
animal_speak(dog)

# 12. Duck Typing
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def flying_test(entity):
    entity.fly()

bird = Bird()
plane = Airplane()

flying_test(bird)
flying_test(plane)

# 13. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)

# 14. Method Overloading & Overriding
class Shape:
    def area(self, x=None, y=None):  # Method overloading (default arguments)
        if x is not None and y is not None:
            return x * y
        elif x is not None:
            return x * x
        else:
            return 0

shape = Shape()
print(shape.area(4, 5))  # Rectangle
print(shape.area(4))  # Square
print(shape.area())  # No input, returns 0

class ParentClass:
    def show(self):
        print("Parent class method")

class ChildClass(ParentClass):
    def show(self):  # Overriding parent method
        print("Child class method")

child = ChildClass()
child.show()  # Calls overridden method
