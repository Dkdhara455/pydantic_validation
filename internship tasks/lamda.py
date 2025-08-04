# Basic Lambda Function (no name)
square = lambda x: x * x
print(square(5))
# Output: 25

# Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 4))
# Output: 7

# Lambda Inside a Function
def make_multiplier(n):
    return lambda x: x * n

times3 = make_multiplier(3)
print(times3(10))
# Output: 30

# Using Lambda with map()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)
# Output: [1, 4, 9, 16]

# Using Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
# Output: [2, 4]

# Using Lambda with sorted() and key
students = [("Alice", 90), ("Bob", 80), ("Deepak", 85)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# Output: [('Bob', 80), ('Deepak', 85), ('Alice', 90)]

# Immediate Use (Inline Lambda)
print((lambda x, y: x * y)(4, 5))
# Output: 20
