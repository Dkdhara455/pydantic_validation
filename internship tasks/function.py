# Defining and Calling a Function
def greet():
    print("Hello, Deepak!")

greet()
# Output: Hello, Deepak!

# Function with Parameters
def add(a, b):
    print("Sum is:", a + b)

add(5, 3)
# Output: Sum is: 8

# Function with Return Value
def square(x):
    return x * x
result = square(4)
print(result)
# Output: 16

# Default Parameters
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Deepak")
# Output:
# Welcome, Guest
# Welcome, Deepak

# Keyword Arguments
def info(name, age):
    print(f"{name} is {age} years old.")

info(age=25, name="Deepak")
# Output: Deepak is 25 years old.

# Variable Length Arguments
def total(*nums):
    print("Total:", sum(nums))

total(1, 2, 3)
# Output: Total: 6

# Return Multiple Values
def stats(x, y):
    return x + y, x * y

s, p = stats(2, 3)
print("Sum:", s)
print("Product:", p)
# Output:
# Sum: 5
# Product: 6

# 🔹 8. Nested Function
def outer():
    def inner():
        print("Inner function")
    print("Outer function")
    inner()

outer()
# Output:
# Outer function
# Inner function
