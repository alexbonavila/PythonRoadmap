# In this file we put a series of python elements


# This is a single-line comment

'''
This is a
multi-line comment
'''

# Variables and Data Types
x = 5  # Integer
y = "World"  # String
z = 4.5  # Float
is_coding = True  # Boolean


# Printing Output
def greet(name):
    print("Hello, " + name + "!")


# If Statements
def compare_values(a, b):
    if a > b:
        print("a is greater than b")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is less than b")


# Loops
def loop_examples():
    # For loop
    for i in range(5):
        print(i)

    # While loop
    j = 0
    while j < 5:
        print(j)
        j += 1


# Lists
my_list = ["apple", "banana", "cherry"]

# Dictionaries
my_dict = {"name": "John", "age": 30}


# Classes/Objects
class MyClass:
    x = 5


# Error Handling
def error_handling_example():
    try:
        print(undefined_variable)
    except NameError:
        print("An exception occurred: variable not defined")


# Imports
import math


def main():
    greet(y)
    compare_values(x, z)
    loop_examples()
    print(my_list[1])  # Accessing the second item: banana
    print(my_dict["name"])  # Accessing the value associated with key "name"
    p1 = MyClass()
    print(p1.x)
    error_handling_example()
    print(math.sqrt(16))  # Using the sqrt function from the math module


if __name__ == "__main__":
    main()
