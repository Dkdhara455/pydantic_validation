# FOR LOOP – Basic
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# FOR LOOP – With List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# FOR LOOP – With Index (using enumerate)
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# WHILE LOOP – Basic
count = 0
while count < 3:
    print("Count:", count)
    count += 1
# Output:
# Count: 0
# Count: 1
# Count: 2

# WHILE LOOP – Countdown
n = 3
while n > 0:
    print(n)
    n -= 1
# Output:
# 3
# 2
# 1

# BREAK in loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# CONTINUE in loop
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4

# ELSE with FOR loop
for i in range(3):
    print(i)
else:
    print("Loop finished!")
# Output:
# 0
# 1
# 2
# Loop finished!

# ELSE with WHILE loop
x = 0
while x < 2:
    print("x =", x)
    x += 1
else:
    print("While loop done!")
# Output:
# x = 0
# x = 1
# While loop done!
