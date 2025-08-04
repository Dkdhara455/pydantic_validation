# Creating a Dictionary
student = {
    "name": "Deepak",
    "age": 25,
    "course": "Python"
}
print(student)
# Output: {'name': 'Deepak', 'age': 25, 'course': 'Python'}

# Accessing Values
print(student["name"])
# Output: Deepak

print(student.get("course"))
# Output: Python

print(student.get("grade", "Not Available"))
# Output: Not Available

# Adding/Updating Key-Value
student["age"] = 26           # Update
student["city"] = "Kolkata"   # Add new
print(student)
# Output: {'name': 'Deepak', 'age': 26, 'course': 'Python', 'city': 'Kolkata'}

# Removing Items
student.pop("city")
print(student)
# Output: {'name': 'Deepak', 'age': 26, 'course': 'Python'}

del student["course"]
print(student)
# Output: {'name': 'Deepak', 'age': 26}

# Looping Through Dictionary
for key, value in student.items():
    print(key, "→", value)
# Output:
# name → Deepak
# age → 26

# Dictionary Keys, Values, Items
print(student.keys())
# Output: dict_keys(['name', 'age'])

print(student.values())
# Output: dict_values(['Deepak', 26])

print(student.items())
# Output: dict_items([('name', 'Deepak'), ('age', 26)])

# Check If Key Exists
print("name" in student)
# Output: True

# Dictionary Length
print(len(student))
# Output: 2

# Nested Dictionary
students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}
print(students["102"]["marks"])
# Output: 90

# Dictionary from List of Tuples
pairs = [("x", 1), ("y", 2)]
d = dict(pairs)
print(d)
# Output: {'x': 1, 'y': 2}