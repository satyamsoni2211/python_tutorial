a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a simple for loop
squared = []
for i in a:
    squared.append(i**2)
print(squared)

# list comprehension
squared_c = [i**2 for i in a]
print(squared_c)

# dictionary comprehension
squared_d = {i: i**2 for i in a}
print(f"{squared_d=}")

# set comprehension
squared_s = {i for i in a}
print(f"{squared_s=}")

# nested comprehension
nested_comprehension = [(i, j) for i in a for j in range(i)]
print(nested_comprehension)

# conditional comprehension
squared_even = [i**2 for i in a if i % 2 == 0]
print(squared_even)

d = {"foo": "abc", "bar": "bcd"}
i = ["foo", "fake"]

transformed_list = [len(value) for key in i if (value := d.get(key))]
print(transformed_list)

for key in i:
    if d.get(key):
        print(key, len(d[key]))
