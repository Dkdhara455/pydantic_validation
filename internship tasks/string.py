# Creating Strings
text = "Hello, Python!"
print(text)
# Output: Hello, Python!

# indexing
print(text[0])  # First character
# Output: H

print(text[-1])  # Last character
# Output: !

# String Slicing
print(text[0:5])  # First 5 letters
# Output: Hello

print(text[7:])  # From index 7 to end
# Output: Python!

print(text[:5])  # From start to index 5 (exclusive)
# Output: Hello

# String Length
print(len(text))
# Output: 14

# String Methods
print(text.lower())   # All lowercase
# Output: hello, python!

print(text.upper())   # All uppercase
# Output: HELLO, PYTHON!

print(text.title())  # Capitalize each word
# Output: Hello, Python!

print(text.replace("Python", "World"))
# Output: Hello, World!

print(text.find("Python"))  # Index of "Python"
# Output: 7

print(text.count("o"))  # Count of 'o'
# Output: 2

# Check Conditions
print(text.startswith("Hello"))
# Output: True

print(text.endswith("!"))
# Output: True

# Whitespace Handling
msg = "   welcome to python   "
print(msg.strip())    # Remove both sides (by default is space)
# Output: welcome to python

print(msg.lstrip())   # Remove left side
# Output: welcome to python

print(msg.rstrip())   # Remove right side
# Output:    welcome to python

# Joining and Splitting
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(joined)
# Output: Python is awesome

split_text = joined.split()
print(split_text)
# Output: ['Python', 'is', 'awesome']

# String Formatting (f-strings)
name = "Deepak"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Deepak and I am 25 years old.

# Escape Characters
quote = "He said, \"Python is easy!\""
print(quote)
# Output: He said, "Python is easy!"
