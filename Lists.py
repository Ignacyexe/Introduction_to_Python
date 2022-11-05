# list is used to store multiple items in one variable

food = ["pizza", "pierogi", "sushi", "spaghetti"]
food[0] = "bigos"   # replaces the element in list
food.append("kebab")    # adds element into list
food.remove("sushi")    # removes element from list
food.insert(0, "cookies")    # adds element to the list between others
food.sort()    # this function will sort the elements alphabetically

# print(food[0])

for x in food:
    print(x)

# lists of lists, more professional is called multidimensional list

drinks = ["coffee", "soda", "tee"]
dinner = ["vegetables", "meat", "potatoes"]
dessert = ["cheesecake", "butterscotch pie"]

meal = [drinks, dinner, dessert]

print("")
print("Introduction to multiple lists!")
print("")
print(meal)

# tuple is a list which is ordered and unchangeable

student = ("Ignacy", 17, "male")

print("")
print("Introduction to tuples!")
print("")
print(student.count("Ignacy"))
print(student.index("male"))
print("")

for x in student:
    print(x)

print("")

if "Ignacy" in student:
    print("Ignacy is student!")


# set - collection which is not indexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife"}
utensils.add("napkin")    # adds item into set
utensils.remove("fork")    # removes item from set
# utensils.clear()   # clears all the items from set

dishes = {"bowl", "plate", "cup"}

# utensils.update(dishes)   # update is used for adding set to another

# dinner_table = utensils.union(dishes)   # it is alternate version of utensils.update

# for x in dinner_table:
#     print(x)

# print(utensils.difference(dishes))   # this will print items which are not common in different sets
print(utensils.intersection(dishes))   # this will print items which are common in different sets

for x in utensils:
    print(x)


# sort() method - used with lists

students = ["Arthur", "Thomas", "John", "Ada", "Finn"]
students.sort(reverse=True)
print()
for i in students:
    print(i)

# sorted() function - used with iterables

students = ("Arthur", "Thomas", "John", "Ada", "Finn")
sorted_students = sorted(students)
print()
for i in sorted_students:
    print(i)
