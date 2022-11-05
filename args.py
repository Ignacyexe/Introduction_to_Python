# args - parameter that will pack all arguments into a tuple. Function can accept a varying amount of arguments

def add(*args):   # this asterisk will pack arguments, and name doesn't matter
    sum = 0
    args = list(args)   # because tuple is not changeable we need to convert this to list
    args[0] = 0   # first item in list will be equal to zero
    for i in args:
        sum += i
    return sum   # this is for escaping the loop


print(add(1, 2, 3, 4, 5))

#  **kwargs - parameter that will pack all the arguments into a dictionary.
# useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs):
    # print("Hello "+kwargs["first"]+" "+kwargs["last"])
    print("Hello ", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Ignacy", middle="Jan", last="Kowalski")
