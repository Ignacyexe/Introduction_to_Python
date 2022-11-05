# loop control statements - it modifies the loop from its original sequence

while True:
    name = input("Enter you name: ")
    if name != "":
        break   # is used to stop loop no matter what

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue    # it skips to another iteration of the loop
    print(i, end="")

for j in range(1, 21):
    if j == 13:
        pass    # this function does nothing and acts as placeholder
    else:
        print(j)
