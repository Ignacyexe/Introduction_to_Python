import time

# while loop - a statement that will execute its block of code,
# as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

# for loop is a statement that will execute its block of code in a limited amount of times

# for i in range(10):
#    print(i + 1)

# for i in range(50, 100+1, 2):
#    print(i)

# for i in "Hello":
#    print(i)

print(" ")

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy New Year!")

# Nested loops - in simple explanation this is loop inside a loop

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter your symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
