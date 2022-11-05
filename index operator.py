# index operator [] - gives access to a sequence's element (str, list, tuples)

name = "Ignacy Kowalski#"

# if(name[0].isupper()):
#     name = name.lower()

first_name = name[0:6].upper()
last_name = name[7:].lower()
last_character = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_character)
