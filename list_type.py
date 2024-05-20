# List Data Type in Python

# Different ways to create a list:
# list() - creates an empty list
# list(iterable) - creates a list from an iterable
# [] - creates an empty list
# [value1, value2, ...] - creates a list with initial values
# list comprehension - creates a list with elements

# Example:
l1 = list()  # empty list
l2 = [1, 2, 3]  # list with initial values
l3 = list([1, 2, 3, 4])  # list from another list
l4 = list("abc")  # list from a string
l5 = [x**2 for x in range(5)]  # list comprehension

# Accessing values in a list:
# Using square brackets [] to access elements by index
print(l2[0])  # >>> 1
print(l2[1:3])  # >>> [2, 3]

# Adding and removing elements:
# append() - adds a single element to the end of the list
# extend() - adds multiple elements to the end of the list
# insert() - inserts an element at a specific index
# remove() - removes the first occurrence of a specific element
# pop() - removes and returns the element at a specific index (default is the last element)
# clear() - removes all elements from the list

l2.append(4)
# >>> l2
# [1, 2, 3, 4]

l2.extend([5, 6])
# >>> l2
# [1, 2, 3, 4, 5, 6]

l2.insert(1, 1.5)
# >>> l2
# [1, 1.5, 2, 3, 4, 5, 6]

l2.remove(1.5)
# >>> l2
# [1, 2, 3, 4, 5, 6]

l2.pop()
# >>> l2
# [1, 2, 3, 4, 5]

l2.pop(1)
# >>> l2
# [1, 3, 4, 5]

l2.clear()
# >>> l2
# []

# List operations:
# + operator to concatenate lists
# * operator to repeat lists
l6 = [1, 2] + [3, 4]
# >>> l6
# [1, 2, 3, 4]

l7 = [1, 2] * 3
# >>> l7
# [1, 2, 1, 2, 1, 2]

# Checking if an element exists in a list:
# Use the 'in' keyword
print(2 in l2)  # >>> False
print(3 in l6)  # >>> True

# Iterating over a list:
# Using a for loop to iterate through the elements of a list
for item in l6:
    print(item)  # >>> 1, 2, 3, 4

# List comprehensions:
# Similar to set comprehensions but used to create lists
squares_list = [x**2 for x in range(5)]
# >>> squares_list
# [0, 1, 4, 9, 16]

# Slicing lists:
# Use the slicing operator to get a subset of a list
print(l6[1:3])  # >>> [2, 3]
print(l6[::-1])  # >>> [4, 3, 2, 1]

# List methods summary:
# append(element) - adds an element to the end of the list
# extend(iterable) - extends the list by appending all elements from the iterable
# insert(index, element) - inserts an element at the specified index
# remove(element) - removes the first occurrence of the element
# pop([index]) - removes and returns the element at the specified index (default is the last element)
# clear() - removes all elements from the list
# index(element, [start, [end]]) - returns the index of the first occurrence of the element
# count(element) - returns the number of occurrences of the element
# sort(key=None, reverse=False) - sorts the elements in ascending order (or in descending order if reverse=True)
# reverse() - reverses the elements of the list in place
# copy() - returns a shallow copy of the list

# Example usage of list methods:
l8 = [3, 1, 4, 1, 5, 9, 2]
print(l8.index(1))  # >>> 1
print(l8.count(1))  # >>> 2
l8.sort()
# >>> l8
# [1, 1, 2, 3, 4, 5, 9]
l8.reverse()
# >>> l8
# [9, 5, 4, 3, 2, 1, 1]
l9 = l8.copy()
# >>> l9
# [9, 5, 4, 3, 2, 1, 1]

# Converting between lists and other data types:
# list() function to convert other data types to a list
list_from_tuple = list((1, 2, 3))
# >>> list_from_tuple
# [1, 2, 3]

list_from_set = list({1, 2, 3})
# >>> list_from_set
# [1, 2, 3]

list_from_string = list("abc")
# >>> list_from_string
# ['a', 'b', 'c']
