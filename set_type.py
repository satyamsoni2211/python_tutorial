# Set Data Type in Python

# Different ways to create a set:
# set() - creates an empty set
# {value1, value2, ...} - creates a set with initial values
# set(iterable) - creates a set from an iterable

# Example:
s1 = set()  # empty set
s2 = {1, 2, 3}  # set with initial values
s3 = set([1, 2, 3, 4])  # set from a list
s4 = set("abc")  # set from a string

# Accessing values in a set:
# Sets do not support indexing or slicing because they are unordered
# You can check for the presence of an element using the 'in' keyword
print(1 in s2)  # >>> True
print(5 in s2)  # >>> False

# Adding and removing elements:
# add() - adds a single element to the set
# update() - adds multiple elements to the set
# remove() - removes a specific element from the set (raises KeyError if not found)
# discard() - removes a specific element from the set (does not raise an error if not found)
# pop() - removes and returns an arbitrary element from the set
# clear() - removes all elements from the set

s2.add(4)
# >>> s2
# {1, 2, 3, 4}

s2.update([5, 6])
# >>> s2
# {1, 2, 3, 4, 5, 6}

s2.remove(6)
# >>> s2
# {1, 2, 3, 4, 5}

s2.discard(5)
# >>> s2
# {1, 2, 3, 4}

s2.pop()  # This removes an arbitrary element
# >>> s2
# {2, 3, 4}

s2.clear()
# >>> s2
# set()

# Set operations:
# union() | - returns a set containing all elements from both sets
# intersection() & - returns a set containing only the elements found in both sets
# difference() - - returns a set containing elements in the first set but not in the second
# symmetric_difference() ^ - returns a set containing elements in either set but not both
# isdisjoint() - returns True if two sets have no elements in common
# issubset() <= - returns True if all elements of one set are in another
# issuperset() >= - returns True if one set contains all elements of another

s5 = {1, 2, 3}
s6 = {3, 4, 5}

union_set = s5 | s6
# >>> union_set
# {1, 2, 3, 4, 5}

intersection_set = s5 & s6
# >>> intersection_set
# {3}

difference_set = s5 - s6
# >>> difference_set
# {1, 2}

sym_diff_set = s5 ^ s6
# >>> sym_diff_set
# {1, 2, 4, 5}

print(s5.isdisjoint(s6))  # >>> False
print(s5.issubset(s6))  # >>> False
print(s5.issuperset({1, 2}))  # >>> True

# Iterating over a set:
# Using a for loop to iterate through the elements of a set
for item in s5:
    print(item)  # >>> 1, 2, 3 (order may vary)

# Frozensets:
# An immutable version of a set
fs1 = frozenset([1, 2, 3, 4])
# fs1.add(5)  # This will raise an AttributeError

# Set comprehensions:
# Similar to list comprehensions but used to create sets
squares_set = {x**2 for x in range(5)}
# >>> squares_set
# {0, 1, 4, 9, 16}

# Converting between lists and sets:
# list() function to convert a set to a list
# set() function to convert a list to a set
list_from_set = list(s5)
# >>> list_from_set
# [1, 2, 3]

set_from_list = set([4, 5, 6])
# >>> set_from_list
# {4, 5, 6}

# Set methods summary:
# add(element) - adds an element to the set
# update(iterable) - updates the set with elements from an iterable
# remove(element) - removes an element from the set, raises KeyError if not found
# discard(element) - removes an element from the set if it is a member
# pop() - removes and returns an arbitrary element from the set
# clear() - removes all elements from the set
# union(set) or | - returns a new set with elements from the set and all others
# intersection(set) or & - returns a new set with elements common to the set and all others
# difference(set) or - - returns a new set with elements in the set that are not in the others
# symmetric_difference(set) or ^ - returns a new set with elements in either the set or others but not both
# isdisjoint(set) - returns True if the set has no elements in common with other
# issubset(set) or <= - returns True if another set contains this set
# issuperset(set) or >= - returns True if this set contains another set
