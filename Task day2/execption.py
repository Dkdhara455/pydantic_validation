# Basic try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
# Output: Cannot divide by zero!

# Multiple Exceptions
try:
    a = int("abc")
except ValueError:
    print("Invalid conversion to integer!")
# Output: Invalid conversion to integer!

#  try-except-else
try:
    n = int(input("Enter a number: "))  # try with valid: 5
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", n)
# Output:
# Enter a number: 5
# You entered: 5


# try-finally
try:
    f = open("data.txt", "w")
    f.write("Logging info")
finally:
    f.close()
    print("File closed.")
# Output: File closed.


# raise – custom exception
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    print("Age set to:", age)

try:
    set_age(-1)
except ValueError as e:
    print("Error:", e)
# Output: Error: Age can't be negative