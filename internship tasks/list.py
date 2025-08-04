# Create a list
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Output: ['apple', 'banana', 'cherry']

# Access elements
print(fruits[0])     # Output: apple
print(fruits[-1])    # Output: cherry

# Update element
fruits[1] = "orange"
print(fruits)
# Output: ['apple', 'orange', 'cherry']

# Add elements
fruits.append("grape")
print(fruits)
# Output: ['apple', 'orange', 'cherry', 'grape']

fruits.insert(1, "kiwi")
print(fruits)
# Output: ['apple', 'kiwi', 'orange', 'cherry', 'grape']

# Remove elements
fruits.remove("apple")
print(fruits)
# Output: ['kiwi', 'orange', 'cherry', 'grape']

fruits.pop()
print(fruits)
# Output: ['kiwi', 'orange', 'cherry']

del fruits[0]
print(fruits)
# Output: ['orange', 'cherry']

#  Length of list
print(len(fruits))
# Output: 2

# Loop
for fruit in fruits:
    print(fruit)
# Output:
# orange
# cherry

# Check if item exists
if "banana" in fruits:
    print("Yes!")
else:
    print("No!")
# Output: No!

# Sort and reverse
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)
# Output: [1, 2, 4, 9]

numbers.reverse()
print(numbers)
# Output: [9, 4, 2, 1]

# List slicing
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print(fruits[1:3])
# Output: ['banana', 'cherry']

print(fruits[:2])
# Output: ['apple', 'banana']

print(fruits[-2:])
# Output: ['date', 'fig']

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# Output: [1, 2, 3, 4]

my_list.extend([5, 6])
print(my_list)
# Output: [1, 2, 3, 4, 5, 6]

my_list.pop(0)
print(my_list)
# Output: [2, 3, 4, 5, 6]
