"""""
Type Casting 
"""""
# Converting an integer to a float
int_to_float = float(5)
print(int_to_float)  # Output: 5.0

# Converting a float to an integer (this will truncate the decimal part)
float_to_int = int(3.14)
print(float_to_int)  # Output: 3

# Converting a number to a string
number_to_string = str(10)
print(number_to_string)  # Output: "10"

# Converting a string to an integer
string_to_int = int("42")
print(string_to_int)  # Output: 42

# Converting a string to a float
string_to_float = float("3.14")
print(string_to_float)  # Output: 3.14


"""""
Exceptions 
"""""
# Handling an exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling multiple exceptions
try:
    # This will raise a ValueError since 'a' cannot be converted to an integer
    number = int("a")
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")

# Using else block (executed if no exception is raised)
try:
    number = int("5")
except ValueError:
    print("Could not convert to integer.")
else:
    print("Conversion successful.")

# Using finally block (always executed)
try:
    number = int("5")
except ValueError:
    print("Could not convert to integer.")
finally:
    print("This will always be executed.")
