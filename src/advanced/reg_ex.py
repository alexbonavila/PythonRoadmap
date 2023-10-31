import re

# Literal Characters
match = re.search(r'abc', '123abc456')
print("Literal Characters:", match.group() if match else 'No match')

# Metacharacters
print("Metacharacter Dot:", re.findall(r'.', 'abc'))
print("Metacharacter ^:", re.findall(r'^abc', 'abcdef'))
print("Metacharacter $:", re.findall(r'abc$', '123abc'))

# Character Classes
print("Character Class [abc]:", re.findall(r'[abc]', 'defghijkl'))
print("Character Class [^abc]:", re.findall(r'[^abc]', 'abcde'))
print("Character Class [a-z]:", re.findall(r'[a-z]', 'ABCdef'))
print("Character Class [A-Z]:", re.findall(r'[A-Z]', 'abcDEF'))
print("Character Class [0-9]:", re.findall(r'[0-9]', 'abc123'))

# Predefined Character Classes
print("Predefined \\d:", re.findall(r'\d', 'abc123'))
print("Predefined \\D:", re.findall(r'\D', '123abc'))
print("Predefined \\s:", re.findall(r'\s', 'foo bar\tbaz\nqux'))
print("Predefined \\S:", re.findall(r'\S', ' \t\nabc'))
print("Predefined \\w:", re.findall(r'\w', '123!@#abc'))
print("Predefined \\W:", re.findall(r'\W', 'abc123!@#'))

# Quantifiers
print("Quantifier *:", re.findall(r'a*', 'baaaac'))
print("Quantifier +:", re.findall(r'a+', 'baaaac'))
print("Quantifier ?:", re.findall(r'a?', 'baaac'))
print("Quantifier {n}:", re.findall(r'a{3}', 'baaaac'))
print("Quantifier {n,}:", re.findall(r'a{2,}', 'baaaac'))
print("Quantifier {n,m}:", re.findall(r'a{1,3}', 'baaaac'))

# Groups and Capturing
match = re.search(r'(abc)', '123abc456')
print("Groups and Capturing:", match.group(1) if match else 'No match')
match = re.search(r'(?:abc)', '123abc456')
print("Non-Capturing Groups:", match.group() if match else 'No match')

# Alternation
print("Alternation:", re.findall(r'a|b', 'cdefabgh'))

# Anchors
print("Anchor \\b:", re.findall(r'\bfoo', 'bar foo baz'))
print("Anchor \\B:", re.findall(r'\Bfoo', 'barfoo baz'))

# Escape Special Characters
print("Escape \\:", re.findall(r'\\', 'E\\F\\G'))

# Lookahead and Lookbehind
print("Lookahead Positive:", re.findall(r'foo(?=bar)', 'foobar foobaz'))
print("Lookahead Negative:", re.findall(r'foo(?!bar)', 'foobar foobaz'))
print("Lookbehind Positive:", re.findall(r'(?<=foo)bar', 'foobar foobaz'))
print("Lookbehind Negative:", re.findall(r'(?<!foo)bar', 'foobar foobaz'))
