class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Deepak", 25)
p1.greet()
# Output: Hello, my name is Deepak and I am 25 years old.

# Inheritance

# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()
# Output:
# Animal speaks
# Dog barks

# Multilevel Inheritance
class Grandparent:
    def home(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.home()
c.car()
c.bike()
# Output:
# Grandparent's house
# Parent's car
# Child's bike

# Multiple Inheritance
class Mother:
    def cook(self):
        print("Mother cooks")

class Father:
    def drive(self):
        print("Father drives")

class Son(Mother, Father):
    def study(self):
        print("Son studies")

s = Son()
s.cook()
s.drive()
s.study()
# Output:
# Mother cooks
# Father drives
# Son studies

# Using super() to Call Parent Constructor
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e = Employee("Deepak", 50000)
e.display()
# Output: Name: Deepak, Salary: 50000

# Encapsulation in Python

# Public Variable (no restriction)
class Car:
    def __init__(self):
        self.speed = 100  # public

c = Car()
print("Speed:", c.speed)
# Output: Speed: 100

# Protected Variable (single underscore)
class Vehicle:
    def __init__(self):
        self._mileage = 20  # protected

v = Vehicle()
print("Mileage:", v._mileage)  # Can access, but not recommended
# Output: Mileage: 20

# Private Variable (double underscore)
class BankAccount:
    def __init__(self):
        self.__balance = 1000  # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = BankAccount()
acc.deposit(500)
print("Balance:", acc.get_balance())
# Output: Balance: 1500

# Trying to access private directly will raise error:
# print(acc.__balance) --> AttributeError

# Name Mangling (accessing private forcefully – not recommended)
print("Hacked Balance:", acc._BankAccount__balance)
# Output: Hacked Balance: 1500

# polimorphism
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def make_sound(animal):
    animal.speak()

make_sound(Cat())
make_sound(Dog())
# Output:
# Meow
# Bark


# Method Overriding (Inheritance)
class Animal:
    def speak(self):
        print("Animal speaks")

class Cow(Animal):
    def speak(self): #this method is overriding
        print("Moo")

a = Animal()
c = Cow()
a.speak()
c.speak()
# Output:
# Animal speaks
# Moo

# Operator Overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(150)
print("Total pages:", b1 + b2)
# Output: Total pages: 250


# Function Overloading (Mimicked using default arguments)
def greet(name=None):
    if name:
        print("Hello", name)
    else:
        print("Hello stranger")

greet("Deepak")
greet()
# Output:
# Hello Deepak
# Hello stranger

# Abstract Class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        print("Usually Petrol or Diesel")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with button")

# Using Abstract Classes
v1 = Car()
v2 = Bike()

v1.start_engine()     # Output: Car engine started with key
v2.start_engine()     # Output: Bike engine started with button
v1.fuel_type()        # Output: Usually Petrol or Diesel

# Can't instantiate abstract class directly:
# v = Vehicle()  # Will raise TypeError