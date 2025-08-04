# Recursive Function
def say_hello(n):
    if n == 0:
        return
    print("Hello!")
    say_hello(n - 1)

say_hello(3)
# Output:
# Hello!
# Hello!
# Hello!

# Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
# Output: 120

#  Fibonacci Series using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(6)])
# Output: [0, 1, 1, 2, 3, 5]

# Sum of Digits using Recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))
# Output: 10

#
#  Reverse a String using Recursion
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("Deepak"))
# Output: kapeeD
