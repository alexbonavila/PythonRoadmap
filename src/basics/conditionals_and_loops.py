"""
Conditionals
"""
# If statement
age = 20
if age >= 18:
    print("You are an adult.")

# If-else statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# If-elif-else statement
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

"""
Loops
"""
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a range of numbers
for i in range(5):  # Will iterate over 0, 1, 2, 3, 4
    print(i)

# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# While loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Break statement
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break

# Continue statement
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)
