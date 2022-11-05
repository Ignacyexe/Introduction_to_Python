# lambda function - function written in 1 line using lambda keyword. Accepts any number of arguments, but only has one
# expression. In simpler explanation lambda is shortcut, and it is temporary solution
# lambda parameters:expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(double(5))
print(multiply(7, 8))
print(add(5, 7, 22))
print(full_name("Ignacy", "Kowalski"))
