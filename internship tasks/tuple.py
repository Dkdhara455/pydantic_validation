# Creating Tuples
t1 = (1, 2, 3)
print(t1)
# Output: (1, 2, 3)

t2 = ("apple", "banana", "cherry")
print(t2)
# Output: ('apple', 'banana', 'cherry')

t3 = (1,)  # Single-element tuple must have a comma
print(type(t3))
# Output: <class 'tuple'>

# Access Elements (Indexing)
print(t2[0])
# Output: apple

print(t2[-1])
# Output: cherry

# Slicing
print(t2[1:3])
# Output: ('banana', 'cherry')

# Loop Through a Tuple
for item in t2:
    print(item)
# Output:
# apple
# banana
# cherry

# Check if Item Exists
print("banana" in t2)
# Output: True

# Tuple Length
print(len(t2))
# Output: 3

# Tuple with Mixed Types
mixed = (1, "hello", True, 3.14)
print(mixed)
# Output: (1, 'hello', True, 3.14)

# Nested Tuples
nested = (1, (2, 3), (4, 5))
print(nested[1])
# Output: (2, 3)

print(nested[1][0])
# Output: 2

# Immutability (Tuples can’t be changed)
# t2[0] = "orange"
# Error: 'tuple' object does not support item assignment

# Convert Tuple to List and Back
temp = list(t2)
temp.append("orange")
t2 = tuple(temp)
print(t2)
# Output: ('apple', 'banana', 'cherry', 'orange')

# Tuple Unpacking
person = ("Deepak", 25, "India")
name, age, country = person
print(name)
# Output: Deepak
print(age)
# Output: 25
print(country)
# Output: India
