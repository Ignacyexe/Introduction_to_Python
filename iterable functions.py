# map - applies a function to each item in an iterable

store = [
    ("shirt", 39.00),
    ("pants", 89.00),
    ("suit", 140.00),
    ("hoodie", 99.00)
]

to_dollar = lambda data: (data[0], round(data[1]/4.63, 2))

store_dollars = (list(map(to_dollar, store)))

for i in store_dollars:
    print(i)

# filter(function, iterable) - creates a collection od elements from an iterable for which a function returns true

friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

print()

age = lambda data1: data1[1] >= 18

allowed_age = list(filter(age, friends))

for i in allowed_age:
    print(i)

# reduce(function, iterable) - apply a function to an iterable and reduce it to a single cumulative value.
# preforms function on first two elements and repeats process until 1 value remains

print()

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y:x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)

# list comprehension - a way to create a new list with less syntax can mimic certain lambda functions, easier to read
# list = [expression (if/else) to item in iterable]

squares = []   # create empty list
for i in range(1, 11):   # create for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

# more optimized version in form of list comprehension

squares = [i * i for i in range(1, 11)]
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
# print(str(list(filter(lambda x: x >= 60, students))))   # still lambda is temporary function, let's optimize it
passed_students = [i for i in students if i >= 60]
print(passed_students)

# dictionary comprehension - create dictionaries using an expression, can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}

cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
cities_in_C = {key: round((value - 32)*(5/9), 2) for (key, value) in cities_in_F.items()}

# dictionary = {key: (if/else) for (key, value) in iterable}

desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key, value) in cities_in_F.items()}

print()
print(cities_in_C)
print(desc_cities)

# dictionary = {key: expression for (key, value) in iterable if conditional}

weather = {"Warsaw": "cloudy", "Gdansk": "snowing", "Cracow": "sunny", "Zakopane": "snowing", "Wroclaw": "sunny"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)
print()

# zip iterables - aggregate elements from two or more iterables. Creates a zip object with paired elements stored in
# tuples for each element within our zip object

usernames = ["john_tea", "ordinary_john", "John_the_Ripper"]
passwords = ("Tea_John123", "P@ssword123", "iloveyou")

users = dict(zip(usernames, passwords))

print(type(users))
for key, value in users.items():
    print(key + " : " + value)
