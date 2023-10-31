# Basic Iterator Usage with `iter` and `next`
my_list = [1, 2, 3, 4]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4


# Custom Iterator Class
class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Count(1, 3)
for c in counter:
    print(c)  # Output: 1, 2, 3

# Iterating Over a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)  # Output: a, b, c

# Iterating Over a File
with open("./resources/files/test.txt", "r") as file:
    for line in file:
        print(line, end='')

# Using `enumerate` for Index-Value Pairs
my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print(counter, value)  # Output: 0 apple, 1 banana, 2 grapes, 3 pear

# Using `zip` to Iterate Over Two Lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(num, letter)  # Output: 1 a, 2 b, 3 c

# List Comprehension Iterator
squared = (x ** 2 for x in range(4))
print(next(squared))  # Output: 0
print(next(squared))  # Output: 1
print(next(squared))  # Output: 4

# Iterating with `iter` Function and a Sentinel
with open("./resources/files/test.txt", "r") as file:
    for line in iter(lambda: file.readline().strip(), ''):
        print(line)
