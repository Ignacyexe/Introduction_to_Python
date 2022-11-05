name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are You?"))
temp = int(input("What is the temperature outside? "))

# that statements below will check which number was put into input
# it is pretty helpful when we need to go through many conditions

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("That age doesn't exist!")
else:
    print("You are not an adult!")

print("Hello " + name)
print("You are " + str(height) + "cm")

# there are logical operators (and, or, not)
# not operator stands for negation, and it reverses the result from the true to false, and false to true

if 0 <= temp <= 30:    # this is less optimized version: temp >= 0 and temp <= 30:
    print("The temperature is normal")
    print("Go outside and TOUCH GRASS")
elif temp < 0 or temp > 30:
    print("The temperature is not normal")
    print("stay inside")
