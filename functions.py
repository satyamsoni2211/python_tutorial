# Functions in Python

# Functions are reusable blocks of code that perform a specific task.
# Functions help in reducing code repetition and improving code readability.


# Defining a function:
# You define a function using the def keyword followed by the function name and parentheses.
def greet():
    """This function prints a greeting message."""
    print("Hello, World!")


# Calling a function:
# You call a function by using its name followed by parentheses.
greet()  # >>> "Hello, World!"


# Function parameters:
# Functions can accept parameters (arguments) to process data.
def greet_person(name):
    """This function prints a personalized greeting message."""
    print(f"Hello, {name}!")


greet_person("Alice")  # >>> "Hello, Alice!"


# Returning values from a function:
# Functions can return values using the return statement.
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b


result = add(5, 3)
print(result)  # >>> 8


# Default parameters:
# You can provide default values for parameters. If no argument is passed, the default value is used.
def greet(name="Guest"):
    """This function prints a greeting message with a default name."""
    print(f"Hello, {name}!")


greet()  # >>> "Hello, Guest"
greet("Bob")  # >>> "Hello, Bob"


# Keyword arguments:
# You can pass arguments using the parameter names.
def describe_person(name, age):
    """This function prints a description of a person."""
    print(f"{name} is {age} years old.")


describe_person(name="Charlie", age=30)  # >>> "Charlie is 30 years old."
describe_person(age=25, name="Diana")  # >>> "Diana is 25 years old."


# Variable-length arguments:
# You can define functions that accept an arbitrary number of arguments using *args and **kwargs.
def sum_all(*args):
    """This function returns the sum of all given arguments."""
    return sum(args)


print(sum_all(1, 2, 3, 4))  # >>> 10


def print_info(**kwargs):
    """This function prints key-value pairs from arbitrary keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Eve", age=22, city="New York")
# >>> name: Eve
# >>> age: 22
# >>> city: New York


# Position-only parameters:
# You can specify that some parameters must be passed positionally using a / in the function signature.
def greet_positional(name, /, greeting="Hello"):
    """This function demonstrates position-only parameters."""
    print(f"{greeting}, {name}!")


greet_positional("Alice")  # >>> "Hello, Alice!"
greet_positional("Bob", "Hi")  # >>> "Hi, Bob"
# greet_positional(name="Charlie")  # This will raise a TypeError


# Keyword-only parameters:
# You can specify that some parameters must be passed by keyword using a * in the function signature.
def greet_keyword(*, name, greeting="Hello"):
    """This function demonstrates keyword-only parameters."""
    print(f"{greeting}, {name}!")


greet_keyword(name="Alice")  # >>> "Hello, Alice!"
greet_keyword(name="Bob", greeting="Hi")  # >>> "Hi, Bob"
# greet_keyword("Charlie")  # This will raise a TypeError

# Lambda functions:
# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can have any number of arguments but only one expression.
add = lambda x, y: x + y
print(add(2, 3))  # >>> 5

# Lambda functions are often used with functions like map(), filter(), and sorted().
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # >>> [1, 4, 9, 16, 25]


# Nested functions:
# You can define functions inside other functions. These are called nested functions or inner functions.
def outer_function(msg):
    """This function contains a nested function."""

    def inner_function():
        print(msg)

    inner_function()


outer_function("Hello from the inner function!")  # >>> "Hello from the inner function!"


# Closures:
# A closure is a nested function that remembers the values from its enclosing scope even after the outer function has finished executing.
def make_multiplier(x):
    def multiplier(n):
        return x * n

    return multiplier


times_three = make_multiplier(3)
print(times_three(10))  # >>> 30


# Function decorators:
# Decorators are a way to modify or enhance functions without changing their definition.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# >>> Something is happening before the function is called.
# >>> Hello!
# >>> Something is happening after the function is called.


# Docstrings:
# Docstrings are string literals that appear right after the definition of a function, method, class, or module.
# They are used to document your code.
def example_function():
    """This is an example of a function with a docstring."""
    pass


print(example_function.__doc__)  # >>> "This is an example of a function with a docstring."


# Function annotations:
# Function annotations are a way of associating various parts of a function with arbitrary python expressions at compile time.
# Annotations are stored in the __annotations__ attribute of the function.
def annotated_function(x: int, y: int) -> int:
    """This function adds two integers."""
    return x + y


print(annotated_function.__annotations__)
# >>> {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

# Function methods summary:
# def function_name(parameters):
#     """Docstring explaining the function."""
#     # Function body
#     return value  # Optional return statement

# Lambda functions summary:
# lambda arguments: expression

# Decorators summary:
# @decorator
# def function():
#     pass

# Position-only parameters summary:
# def function_name(pos1, pos2, /, param1, param2):
#     # Function body

# Keyword-only parameters summary:
# def function_name(*, param1, param2):
#     # Function body
