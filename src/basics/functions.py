"""""
User-defined Functions 
"""""


# Defining a simple function
def greet():
    print("Hello, World!")


# Calling the function
greet()


# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Alice")


# Function with default parameter value
def greet_person_with_default(name="World"):
    print(f"Hello, {name}!")


greet_person_with_default()
greet_person_with_default("Bob")


# Function returning a value
def add(a, b):
    return a + b


result = add(3, 4)
print(result)  # Output: 7


# Function with variable number of arguments
def sum_numbers(*args):
    return sum(args)


total = sum_numbers(1, 2, 3, 4)
print(total)  # Output: 10


# Function with keyword arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")


describe_person(age=30, name="Alice")


# Function with variable number of keyword arguments
def describe_person_v2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")


describe_person_v2(name="Bob", age=25, location="New York")


"""""
Built-in Functions
"""""
# The len() function
length = len("Hello")
print(length)  # Output: 5

# The abs() function
absolute_value = abs(-5)
print(absolute_value)  # Output: 5

# The round() function
rounded_number = round(3.14159, 2)
print(rounded_number)  # Output: 3.14

# The type() function
data_type = type(10)
print(data_type)  # Output: <class 'int'>

# The range() function
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# The input() function
user_input = input("Enter something: ")
print(user_input)

# The print() function
print("Hello, World!")

# The str(), int(), float() functions (for type casting)
string_to_number = int("42")
print(string_to_number)  # Output: 42
