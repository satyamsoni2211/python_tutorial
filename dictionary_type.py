# Dictionary Data Type in Python

# Different ways to create a dictionary:
# dict() - creates an empty dictionary
# {} - creates an empty dictionary
# {'key1': 'value1', 'key2': 'value2'} - creates a dictionary with initial key-value pairs
# dict(key1='value1', key2='value2') - creates a dictionary with initial key-value pairs using keyword arguments
# dict([(key1, value1), (key2, value2)]) - creates a dictionary from a list of key-value pairs
# dict(zip(keys, values)) - creates a dictionary from two lists, one with keys and one with values

# Example:
d1 = dict()  # or {}
d2 = {"name": "Alice", "age": 25}
d3 = dict(name="Bob", age=30)
d4 = dict([("name", "Charlie"), ("age", 35)])
d5 = dict(zip(["name", "age"], ["David", 40]))

# Accessing values in a dictionary:
# Using square brackets [] - raises a KeyError if the key is not found
# Using the get() method - returns None or a default value if the key is not found
print(d2["name"])  # >>> 'Alice'
print(d2.get("age"))  # >>> 25
print(d2.get("address", "Not Found"))  # >>> 'Not Found'

# Adding and updating key-value pairs:
# Use square brackets [] to add or update a key-value pair
d2["address"] = "123 Main St"  # Adds a new key-value pair
d2["age"] = 26  # Updates the value of an existing key
# >>> d2
# {'name': 'Alice', 'age': 26, 'address': '123 Main St'}

# Removing key-value pairs:
# pop() - removes the key-value pair for the given key and returns the value
# popitem() - removes and returns the last key-value pair as a tuple
# del - deletes the key-value pair for the given key
# clear() - removes all key-value pairs
d2.pop("address")  # >>> '123 Main St'
d2.popitem()  # >>> ('age', 26)
del d2["name"]
# >>> d2
# {}

# Checking if a key exists in a dictionary:
# Use the 'in' keyword
print("name" in d3)  # >>> True
print("age" in d3)  # >>> True

# Iterating over a dictionary:
# keys() - returns a view of the dictionary's keys
# values() - returns a view of the dictionary's values
# items() - returns a view of the dictionary's key-value pairs
for key in d3.keys():
    print(key)  # >>> 'name', 'age'

for value in d3.values():
    print(value)  # >>> 'Bob', 30

for key, value in d3.items():
    print(f"{key}: {value}")  # >>> 'name: Bob', 'age: 30'

# Dictionary comprehensions:
# Similar to list comprehensions but used to create dictionaries
# Example: Create a dictionary with keys as numbers and values as their squares
squares = {x: x**2 for x in range(5)}
# >>> squares
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging dictionaries:
# Use the update() method to add key-value pairs from one dictionary to another
# Use the ** unpacking operator in Python 3.5+
d6 = {"a": 1, "b": 2}
d7 = {"b": 3, "c": 4}
d6.update(d7)  # >>> {'a': 1, 'b': 3, 'c': 4}
d8 = {**d6, **d7}  # >>> {'a': 1, 'b': 3, 'c': 4}

# Dictionary methods summary:
# dict() - creates a dictionary
# get(key[, default]) - returns the value for key if key is in the dictionary, else default
# keys() - returns a view object of the dictionary's keys
# values() - returns a view object of the dictionary's values
# items() - returns a view object of the dictionary's key-value pairs
# pop(key[, default]) - removes the specified key and returns the corresponding value
# popitem() - removes and returns the last key-value pair as a tuple
# clear() - removes all items from the dictionary
# update([other]) - updates the dictionary with the key-value pairs from other, overwriting existing keys
# setdefault(key[, default]) - returns the value of key if it is in the dictionary; if not, inserts key with a value of default and returns default
# copy() - returns a shallow copy of the dictionary
# fromkeys(iterable[, value]) - creates a new dictionary with keys from iterable and values set to value
