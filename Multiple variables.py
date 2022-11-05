# name = "Ignacy"  Introduction to multiple variables which optimizes code
# age = 21
# attractive = True

name, age, attractive = "Ignacy", 17, True

# Mariusz = 30  This is optimizing code for variables which have the same value
# Maniek = 30
# Marcinek = 30

Mariusz = Maniek = Marcinek = 30

print(name)
print(age)
print(attractive)
print(" ")
print(Mariusz)
print(Maniek)
print(Marcinek)

print(" ")

print(len(name))    # it shows length of the string
print(name.find("g"))   # finds in which position from zero is compared letter
print(name.capitalize())    # this method will turn first letter uppercase
print(name.upper())    # this method will turn all letters uppercase
print(name.lower())    # this method will turn all letters lowercase
print(name.isdigit())   # this method will print if the string is a digit or not
print(name.isalpha())   # this method will print if the string is a letter or not
print(name.count("a"))     # this method will count letters of string
print(name.replace("y", " ")+"I hate it when someone calls me like that")  # this method will replace letters in string
print(name*3)
