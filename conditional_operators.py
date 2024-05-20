# Conditional Statements in Python

# Conditional statements allow you to execute different blocks of code based on certain conditions.
# The main conditional statements in Python are if, elif, else, and match.

# if statement:
# The if statement executes a block of code if a specified condition is true.
x = 10
if x > 5:
    print("x is greater than 5")  # >>> "x is greater than 5"

# elif statement:
# The elif (short for "else if") statement checks another condition if the previous conditions were false.
x = 10
if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is equal to 10")  # >>> "x is equal to 10"

# else statement:
# The else statement executes a block of code if none of the previous conditions were true.
x = 10
if x < 5:
    print("x is less than 5")
elif x == 7:
    print("x is equal to 7")
else:
    print(
        "x is neither less than 5 nor equal to 7"
    )  # >>> "x is neither less than 5 nor equal to 7"

# Nested if statements:
# You can nest if statements inside other if statements to check multiple conditions.
x = 10
y = 20
if x > 5:
    if y > 15:
        print(
            "x is greater than 5 and y is greater than 15"
        )  # >>> "x is greater than 5 and y is greater than 15"

# One-line if statement (ternary operator):
# Python also supports a shorthand syntax for the if-else statement.
x = 10
(
    print("x is greater than 5") if x > 5 else print("x is not greater than 5")
)  # >>> "x is greater than 5"

# Logical operators in conditions:
# You can use logical operators (and, or, not) to combine multiple conditions.
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")  # >>> "Both conditions are true"

if x > 15 or y > 15:
    print("At least one condition is true")  # >>> "At least one condition is true"

if not x < 5:
    print("x is not less than 5")  # >>> "x is not less than 5"

# Using comparison operators in conditions:
# Python supports several comparison operators to compare values in conditional statements.
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

x = 10
if x == 10:
    print("x is equal to 10")  # >>> "x is equal to 10"

if x != 5:
    print("x is not equal to 5")  # >>> "x is not equal to 5"

if x > 5:
    print("x is greater than 5")  # >>> "x is greater than 5"

if x < 15:
    print("x is less than 15")  # >>> "x is less than 15"

if x >= 10:
    print("x is greater than or equal to 10")  # >>> "x is greater than or equal to 10"

if x <= 20:
    print("x is less than or equal to 20")  # >>> "x is less than or equal to 20"

# Using membership operators in conditions:
# Python supports membership operators (in, not in) to check if a value is present in a sequence.
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list")  # >>> "3 is in the list"

if 6 not in my_list:
    print("6 is not in the list")  # >>> "6 is not in the list"

# Using identity operators in conditions:
# Python supports identity operators (is, is not) to compare the memory locations of two objects.
a = [1, 2, 3]
b = a
c = [1, 2, 3]

if a is b:
    print("a and b are the same object")  # >>> "a and b are the same object"

if a is not c:
    print("a and c are not the same object")  # >>> "a and c are not the same object"


# match-case statement:
# The match-case statement is used for pattern matching, introduced in Python 3.10.
# It allows you to match variables against a sequence of patterns.
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


print(http_status(200))  # >>> "OK"
print(http_status(404))  # >>> "Not Found"
print(http_status(999))  # >>> "Unknown Status"


# Pattern matching with multiple values:
def point_location(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y-axis at y={y}"
        case (x, 0):
            return f"X-axis at x={x}"
        case (x, y):
            return f"Point at x={x}, y={y}"
        case _:
            return "Unknown point"


print(point_location((0, 0)))  # >>> "Origin"
print(point_location((0, 5)))  # >>> "Y-axis at y=5"
print(point_location((3, 0)))  # >>> "X-axis at x=3"
print(point_location((3, 4)))  # >>> "Point at x=3, y=4"
print(point_location((None, None)))  # >>> "Unknown point"

# Conditional statements summary:
# if condition:
#     # block of code to be executed if the condition is true
#
# elif condition:
#     # block of code to be executed if the previous conditions were false and this condition is true
#
# else:
#     # block of code to be executed if all the previous conditions were false
#
# match value:
#     case pattern1:
#         # block of code to be executed if value matches pattern1
#     case pattern2:
#         # block of code to be executed if value matches pattern2
#     case _:
#         # block of code to be executed if value does not match any of the above patterns
