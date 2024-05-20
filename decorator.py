# Decorators in Python

# Decorators are functions that modify the behavior of other functions or methods.

# Importing necessary module
import functools


# Closures:
# Closures are functions that remember the values from their enclosing lexical scope even after the scope has finished executing.
def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function


closure_func = outer_function("Hello from the closure!")
closure_func()  # >>> "Hello from the closure!"


# Simple decorator:
# A simple decorator modifies the behavior of a function without changing its definition.
def my_decorator(func):
    @functools.wraps(func)
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


# Decorators with validation:
# Decorators can perform validation checks before executing the wrapped function.
def validate(func):
    @functools.wraps(func)
    def wrapper(age):
        if age < 18:
            print("You are not eligible.")
        else:
            func(age)

    return wrapper


@validate
def enter_club(age):
    print("Welcome to the club!")


enter_club(20)  # >>> "Welcome to the club!"
enter_club(16)  # >>> "You are not eligible."


# Decorator with arguments:
# Decorators can take arguments for customization.
def repeat(num_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
# >>> Hello, Alice!
# >>> Hello, Alice!
# >>> Hello, Alice!


# Class-based decorator:
# Decorators can also be implemented using classes.
class DecoratorClass:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print("Decorator class executed before function.")
        self.func(*args, **kwargs)
        print("Decorator class executed after function.")


@DecoratorClass
def say_hi(name):
    print(f"Hi, {name}!")


say_hi("Bob")
# >>> Decorator class executed before function.
# >>> Hi, Bob!
# >>> Decorator class executed after function.


# Decorator for singleton function:
# Decorators can be used to create singleton functions, ensuring that only one instance of the function exists.
def singleton(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = func(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
def get_database_connection():
    return "Database connection established"


print(get_database_connection())  # >>> "Database connection established"
print(get_database_connection())  # >>> "Database connection established"
# Both calls return the same instance of the database connection.

# Why use functools.wraps:
# - Preserves the identity of the original function: Without functools.wraps, the decorated function would lose its identity, making debugging and introspection more challenging.

# Consequences of not using functools.wraps:
# - Original function metadata is lost: The function name, docstring, and other metadata of the original function would not be preserved, which can lead to confusion and errors when debugging or using introspection tools.
# - Decorator chain issues: Without preserving the identity of the original function, decorators applied on top of each other may not behave as expected, leading to unpredictable behavior.

# Summary:
# - Closures:
#   - Functions that remember values from their enclosing lexical scope.
# - Simple decorator:
#   - Modifies the behavior of a function without changing its definition.
# - Decorators with validation:
#   - Performs validation checks before executing the wrapped function.
# - Decorator with arguments:
#   - Takes arguments for customization.
# - Class-based decorator:
#   - Implemented using classes to modify function behavior.
# - Decorator for singleton function:
#   - Ensures only one instance of the function exists.
