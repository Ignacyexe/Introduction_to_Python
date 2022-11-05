# return statement - functions send Python values/objects back to the caller. These are known as the function return val

def multiply(number1, number2):
    return number1 * number2


print(multiply(34, 3))


# scope - a region that a variable is recognized. A variable is only recognized from inside the region it is created
# a global and locally scoped versions of a variable can be created

first_name = "Jan"   # this is global scope which is available outside and inside of function.


def display_name():
    name = "Ignacy"   # local scope (which is available only inside this function)
    print(name)


# print(name)   # trying to print this variable will cause error called: "NameError: name 'name' is not defined" because
# it is outside a local scope

print(first_name)
