# string format (str.format()) - optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))  # positional arguments, whe can replace values in this method
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))   # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Ignacy"
print("Hello my name is {:15}. Nice to meet you".format(name))   # colon is adjusting the padding in format
print("Hello my name is {:<15}. Nice to meet you".format(name))   # left align
print("Hello my name is {:>15}. Nice to meet you".format(name))   # right align
print("Hello my name is {:^15}. Nice to meet you".format(name))   # center align

number = 3.14159
print("The number pi is {:.2f}".format(number))  # f stands for floating number and two for digits after decimal portion

binary = 3498
print("The number {0} in binary will be {0:b}".format(binary))   # b stands for translation decimal nuber to binary

hexadecimal = 5574
print("The number {0} in hexadecimal will be {0:X}".format(hexadecimal))
