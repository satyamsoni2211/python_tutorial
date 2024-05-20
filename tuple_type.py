# Tuple Data Type in Python

# Different ways to create a tuple:
# () - creates an empty tuple
# (value,) - creates a tuple with a single value (comma is necessary)
# (value1, value2, ...) - creates a tuple with multiple values
# tuple() - creates an empty tuple or converts an iterable to a tuple
# tuple(iterable) - creates a tuple from an iterable

# Example:
t1 = ()  # empty tuple
t2 = (1,)  # single value tuple
t3 = (1, 2, 3)  # multiple values tuple
t4 = tuple()  # empty tuple using tuple()
t5 = tuple([1, 2, 3])  # tuple from a list
t6 = tuple("abc")  # tuple from a string

# Accessing values in a tuple:
# Using square brackets [] to access elements by index
print(t3[0])  # >>> 1
print(t3[1:])  # >>> (2, 3)

# Tuples are immutable:
# Once created, elements of a tuple cannot be changed, added, or removed
# t3[0] = 10  # This will raise a TypeError

# Tuple unpacking:
# Assigning the elements of a tuple to multiple variables
a, b, c = t3
# >>> a, b, c
# 1, 2, 3

# Nested tuples:
# Tuples can contain other tuples as elements
t7 = (1, (2, 3), (4, 5, 6))
print(t7[1])  # >>> (2, 3)
print(t7[1][0])  # >>> 2

# Tuple methods:
# count() - returns the number of times a specified value occurs in a tuple
# index() - returns the first index of the specified value
print(t3.count(2))  # >>> 1
print(t3.index(2))  # >>> 1

# Iterating over a tuple:
# Using a for loop to iterate through the elements of a tuple
for item in t3:
    print(item)  # >>> 1, 2, 3

# Tuple concatenation and repetition:
# + operator to concatenate tuples
# * operator to repeat tuples
t8 = t2 + t3
# >>> t8
# (1, 1, 2, 3)

t9 = t2 * 3
# >>> t9
# (1, 1, 1)

# Checking if an element exists in a tuple:
# Use the 'in' keyword
print(2 in t3)  # >>> True
print(4 in t3)  # >>> False

# Comparing tuples:
# Tuples are compared lexicographically using comparison operators
print((1, 2, 3) < (1, 2, 4))  # >>> True
print((1, 2, 3) > (1, 1, 4))  # >>> True

# Slicing tuples:
# Use the slicing operator to get a subset of a tuple
print(t3[1:3])  # >>> (2, 3)
print(t3[::-1])  # >>> (3, 2, 1)

# Converting between lists and tuples:
# list() function to convert a tuple to a list
# tuple() function to convert a list to a tuple
list_from_tuple = list(t3)
# >>> list_from_tuple
# [1, 2, 3]

tuple_from_list = tuple([4, 5, 6])
# >>> tuple_from_list
# (4, 5, 6)

# Tuple comprehensions:
# While there is no "tuple comprehension", we can use generator expressions
# and convert them to tuples
gen_expr = (x**2 for x in range(5))
tuple_from_gen = tuple(gen_expr)
# >>> tuple_from_gen
# (0, 1, 4, 9, 16)

# Tuple methods summary:
# count(value) - returns the number of occurrences of value
# index(value) - returns the first index of value
