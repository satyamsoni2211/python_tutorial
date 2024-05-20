# Loops in Python

# Loops are used to execute a block of code repeatedly until a certain condition is met.

# For loop:
# The for loop is used to iterate over a sequence (list, tuple, string, etc.).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # >>> "apple", "banana", "cherry"

# For else:
# The else block is executed when the loop terminates naturally (without encountering a break statement).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print(
        "Loop completed successfully"
    )  # >>> "apple", "banana", "cherry", "Loop completed successfully"

# While loop:
# The while loop is used to execute a block of code as long as a condition is true.
i = 0
while i < 5:
    print(i)
    i += 1  # Increment the counter
# Output:
# >>> 0
# >>> 1
# >>> 2
# >>> 3
# >>> 4

# While else:
# The else block is executed when the condition becomes false.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Condition is false")  # >>> 0, 1, 2, 3, 4, "Condition is false"

# Comprehensions:
# Comprehensions provide a concise way to create sequences like lists, dictionaries, and sets.
# List comprehension:
squares = [x**2 for x in range(5)]
print(squares)  # >>> [0, 1, 4, 9, 16]

# Dictionary comprehension:
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # >>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension:
squares_set = {x**2 for x in range(5)}
print(squares_set)  # >>> {0, 1, 4, 9, 16}

# Break statements:
# The break statement is used to exit the loop prematurely.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break  # Exit the loop when 'banana' is encountered
# Output:
# >>> "apple", "banana"

# Skipping loop iterations using continue:
# The continue statement is used to skip the rest of the code inside the loop for the current iteration and proceed to the next iteration.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue  # Skip 'banana' and continue with the next iteration
    print(fruit)
# Output:
# >>> "apple", "cherry"

# Loop summary:
# - For loop:
#   for variable in sequence:
#       # Code block

# - For else:
#   for variable in sequence:
#       # Code block
#   else:
#       # Code block executed when the loop terminates normally

# - While loop:
#   while condition:
#       # Code block

# - While else:
#   while condition:
#       # Code block
#   else:
#       # Code block executed when the condition becomes false

# - Comprehensions:
#   [expression for item in iterable]
#   {key_expression: value_expression for item in iterable}
#   {expression for item in iterable}

# - Break statements:
#   break

# - Skipping loop iterations using continue:
#   continue
