# function - a block of code which is executed only when it is called.

def hello(age, name):
    print("Hello " + name)
    print("You are "+str(age)+" years old!")
    print("Have a nice day!")

# first_name = input("How's your name? ")


hello(17, name=input("How's your name? "))

# keyword arguments - arguments preceded by an identifier when we pass them to a function.
# the order of the arguments doesn't matter, unlike positional arguments.
# python knows tha names of the arguments that our function receives

print(" ")


def hi(first, middle, last):
    print("Hi "+first+" "+middle+" "+last)


hi(last="Kowalski", first="Ignacy", middle="Jan")
