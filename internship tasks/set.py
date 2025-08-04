# Creating Sets
s1 = {1, 2, 3, 4}
print(s1)
# Output: {1, 2, 3, 4}

s2 = set([3, 4, 5, 6])
print(s2)
# Output: {3, 4, 5, 6}

# Sets remove duplicates automatically
s3 = {1, 2, 2, 3, 3}
print(s3)
# Output: {1, 2, 3}

# Add and Remove Elements
s1.add(5)
print(s1)
# Output: {1, 2, 3, 4, 5}

s1.remove(2)
print(s1)
# Output: {1, 3, 4, 5}

s1.discard(10)  # No error even if not found
print(s1)
# Output: {1, 3, 4, 5}

# Set Operations
print(s1.union(s2))
# Output: {1, 3, 4, 5, 6}

print(s1.intersection(s2))
# Output: {3, 4, 5}

print(s1.difference(s2))
# Output: {1}

print(s1.symmetric_difference(s2))
# Output: {1, 6}

# Loop Through Set
for item in s1:
    print(item)
# Output (unordered):
# 1
# 3
# 4
# 5

# Check Membership
print(4 in s1)
# Output: True

print(7 in s1)
# Output: False

# Set Length
print(len(s1))
# Output: 4

# Frozen Set (Immutable version of set)
fs = frozenset([10, 20, 30])
print(fs)
# Output: frozenset({10, 20, 30})

fs.add(40) 
# Error: 'frozenset' object has no attribute 'add'

# Frozen set in dictionary key (hashable)
data = {fs: "frozen data"}
print(data)
# Output: {frozenset({10, 20, 30}): 'frozen data'}
