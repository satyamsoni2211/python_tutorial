# Generator functions:
# Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement to return values one at a time.
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))  # >>> 1
print(next(gen))  # >>> 2
print(next(gen))  # >>> 3
# print(next(gen))  # This will raise a StopIteration exception

# Generator expressions:
# Similar to list comprehensions but for generators. They use parentheses instead of square brackets.
gen_expr = (x**2 for x in range(5))
print(next(gen_expr))  # >>> 0
print(next(gen_expr))  # >>> 1
print(next(gen_expr))  # >>> 4
print(next(gen_expr))  # >>> 9
print(next(gen_expr))  # >>> 16
