"""
Lists
"""
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list elements
print(fruits[0])  # Output: apple

# Adding an element to the end of the list
fruits.append("orange")

# Inserting an element at a specific position
fruits.insert(1, "blueberry")

# Removing an element
fruits.remove("banana")

# Removing an element by index
del fruits[0]

# Slicing a list
sublist = fruits[1:3]

# List comprehension
squared_numbers = [x**2 for x in range(10)]


"""
Tuples
"""
# Creating a tuple
coordinates = (10.0, 20.0)

# Accessing tuple elements
print(coordinates[0])  # Output: 10.0

# Tuples cannot be changed after creation (immutable)
# coordinates[0] = 15.0  # This would raise an error

# Tuple unpacking
x, y = coordinates

"""
Sets
"""
# Creating a set
unique_numbers = {1, 2, 3, 4, 5}

# Adding an element to a set
unique_numbers.add(6)

# Removing an element from a set
unique_numbers.remove(3)

# Checking for membership
print(2 in unique_numbers)  # Output: True

# Set operations (union, intersection, difference)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b  # Output: {1, 2, 3, 4, 5}
intersection_set = set_a & set_b  # Output: {3}
difference_set = set_a - set_b  # Output: {1, 2}

"""
Dictionaries
"""
# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing dictionary elements
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Removing a key-value pair
del person["age"]

# Using the get method to avoid KeyError
age = person.get("age", "Age not found")

# Iterating over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squared_numbers_dict = {x: x**2 for x in range(5)}
