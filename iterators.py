# Iterators in Python

# What are iterators?
# Iterators are objects that allow you to traverse through all the elements of a collection (such as lists, tuples, or sets) one at a time.
# In Python, an iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().

# Creating an iterator:
# You can create an iterator from any iterable (like lists, tuples, etc.) using the iter() function.
# You can get the next value from an iterator using the next() function.

# Example:
l1 = [1, 2, 3, 4]
iter_l1 = iter(l1)  # Create an iterator from the list
print(next(iter_l1))  # >>> 1
print(next(iter_l1))  # >>> 2
print(next(iter_l1))  # >>> 3
print(next(iter_l1))  # >>> 4
# print(next(iter_l1))  # This will raise a StopIteration exception

# Custom iterators:
# You can create your own custom iterator by defining a class that implements the __iter__() and __next__() methods.


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


my_iter = MyIterator([10, 20, 30])
print(next(my_iter))  # >>> 10
print(next(my_iter))  # >>> 20
print(next(my_iter))  # >>> 30
# print(next(my_iter))  # This will raise a StopIteration exception

# Using iterators with loops:
# The most common use of iterators is within loops, particularly for loops, which automatically handle the iteration protocol.

for value in MyIterator([100, 200, 300]):
    print(value)  # >>> 100, 200, 300

# Infinite iterators:
# Itertools provides tools to create infinite iterators, such as count(), cycle(), and repeat().
from itertools import count, cycle, repeat

# count() - creates an iterator that generates consecutive integers, starting from a specified number
counter = count(start=5, step=2)
print(next(counter))  # >>> 5
print(next(counter))  # >>> 7
print(next(counter))  # >>> 9

# cycle() - creates an iterator that cycles through an iterable indefinitely
cycler = cycle([1, 2, 3])
print(next(cycler))  # >>> 1
print(next(cycler))  # >>> 2
print(next(cycler))  # >>> 3
print(next(cycler))  # >>> 1

# repeat() - creates an iterator that repeats an object indefinitely, or a specified number of times
repeater = repeat("A", 3)
print(next(repeater))  # >>> 'A'
print(next(repeater))  # >>> 'A'
print(next(repeater))  # >>> 'A'
# print(next(repeater))  # This will raise a StopIteration exception

# Iterator methods summary:
# __iter__() - returns the iterator object itself
# __next__() - returns the next value and advances the iterator. Raises StopIteration when there are no more items.
