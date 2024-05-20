# Python Exceptions and Custom Exceptions

# Python provides a robust exception handling mechanism to deal with runtime errors or exceptional situations in code.

# Exceptions:
# An exception is an event that interrupts the normal flow of a program's execution. When an exception occurs, the program terminates abruptly unless it is handled properly.

# Handling Exceptions:
# Exceptions can be handled using the try-except block, which allows you to catch and handle specific exceptions gracefully.

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Division by zero error occurred")

# Multiple Except Blocks:
# You can use multiple except blocks to handle different types of exceptions.

try:
    # Code that may raise an exception
    result = int("abc")
except ValueError:
    # Handle value error
    print("Value error occurred")
except ZeroDivisionError:
    # Handle zero division error
    print("Division by zero error occurred")

# Generic Except Block:
# You can use a generic except block to catch any exception not handled by previous except blocks.

try:
    # Code that may raise an exception
    result = int("abc")
except ValueError:
    # Handle value error
    print("Value error occurred")
except ZeroDivisionError:
    # Handle zero division error
    print("Division by zero error occurred")
except:
    # Handle any other exception
    print("An error occurred")

# Finally Block:
# The finally block is used to execute cleanup code regardless of whether an exception occurs or not.

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Division by zero error occurred")
finally:
    # Cleanup code
    print("Cleanup code executed")

# Custom Exceptions:
# You can create custom exceptions by subclassing the built-in Exception class.


class CustomError(Exception):
    pass


try:
    raise CustomError("Custom error message")
except CustomError as e:
    print("Custom error handled:", e)

# Custom Exceptions with Arguments:
# You can pass arguments to custom exceptions to provide additional context.


class ValueTooSmallError(Exception):
    def __init__(self, value):
        self.value = value


try:
    raise ValueTooSmallError(5)
except ValueTooSmallError as e:
    print("ValueTooSmallError: The value is too small:", e.value)

# Best Practices for Error Handling:
# - Be specific with exception handling: Catch only the exceptions you expect and handle them appropriately.
# - Use meaningful error messages: Provide informative error messages that help in understanding the cause of the exception.
# - Avoid empty except blocks: Catching all exceptions indiscriminately can hide bugs and make debugging difficult.
# - Use finally blocks for cleanup: Ensure that necessary cleanup tasks are executed, even if an exception occurs.
# - Consider logging: Logging exceptions can help in debugging and troubleshooting issues in production environments.
# - Use custom exceptions for specific cases: Create custom exceptions to represent specific error conditions in your application.

# Summary:
# - Exceptions allow you to gracefully handle runtime errors or exceptional situations in code.
# - Use try-except blocks to handle exceptions.
# - Multiple except blocks can be used to handle different types of exceptions.
# - A generic except block can catch any exception not handled by previous blocks.
# - The finally block is used to execute cleanup code regardless of whether an exception occurs or not.
# - Custom exceptions can be created by subclassing the built-in Exception class.
# - Custom exceptions can have arguments to provide additional context.
