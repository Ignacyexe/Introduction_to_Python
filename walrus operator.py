say = print   # this is assigning function to variable
say("Hi!")

# walrus operator (:=) aka assignment expression and assigns values to variables as part of a larger expression

# full_of_soup = True
# print(full_of_soup)

# print(full_of_soup := True)

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while food := input("What food do you like? ") != "quit":
    foods.append(food)
