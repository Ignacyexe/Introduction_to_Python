import random

x = random.randint(1, 6)
print(x)

y = random.random()   # generates number between 0 and 1
print(y)

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)   # this function will change randomly the order of list
print(numbers)
