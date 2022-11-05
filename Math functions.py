import math

pi = 3.14
ip = 4.12
api = 2.78

print(round(pi))
print(math.ceil(pi))    # this math function will round number by up
print(math.floor(pi))
print(abs(pi))    # stands from absolute number. This math function will show how far is number from zero
print(pow(pi, 2))    # it calculates the number into the power of 2
print(math.sqrt(625))    # this function will take the number and put it into square root
print(max(pi, ip, api))
print(min(pi, ip, api))

# nested function calls - function calls inside other function calls innermost are
# resolved first returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))
