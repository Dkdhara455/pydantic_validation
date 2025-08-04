#if, elif, else
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
# Output: Positive

# Nested if
num = 5
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
# Output: Positive Odd

# break – exit loop early
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# continue – skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4

# pass – placeholder (does nothing)
for i in range(3):
    if i == 1:
        pass  # Used when code is not written yet
    print("Value:", i)
# Output:
# Value: 0
# Value: 1
# Value: 2
