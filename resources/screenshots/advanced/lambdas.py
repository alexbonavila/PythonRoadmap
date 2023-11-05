from functools import reduce

# Basic Lambda Function
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Lambda with `map`
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Lambda with `filter`
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]

# Lambda with `reduce`
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Lambda in List Comprehensions
funcs = [lambda x, n=n: x + n for n in range(5)]
for func in funcs:
    print(func(0))  # Output: 0, 1, 2, 3, 4

# Lambda with `sorted`
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Lambda as an Immediate Function
print((lambda x, y: x + y)(5, 3))  # Output: 8

# Lambda in a Dictionary
switch = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}
print(switch['add'](4, 5))  # Output: 9
print(switch['subtract'](4, 5))  # Output: -1
