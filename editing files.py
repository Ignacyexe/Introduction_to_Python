import os
import shutil
import time

# checking files in python

path = "C:\\Users\\Ignacy\\Desktop\\test.txt"

destination = "C:\\Users\\Ignacy\\Documents\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist!")

# editing text in python

text = "This is my first file edited in python\n I think this will be pretty useful in many cases"

with open(path, "w") as file:
    file.write(text)

# reading files in python

try:
    with open(path) as file:
        print(end=" ")
        print(file.read())
except FileNotFoundError:
    print("That file was not found...")

# copying files in python

# there is three types of copying in python:
# - copyfile() - copies contents of file
# - copy() - copyfile() + permission mode + destination can be a directory
# - copy2() - copy() + copies metadata of file

shutil.copyfile(path, "C:\\Users\\Ignacy\\Desktop\\copy.txt")   # this function does have two arguments: srs and dst

print(" ")   # moving files in python

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(path, destination)
        print(path + " was moved")
except FileNotFoundError:
    print(path + " was not found...")

# timer :)


n = 10
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("File should be deleted")


# deleting files in python

try:
    # os.rmdir() - this is a function which deletes empty folders
    # shutil.rmtree() - this is a function which deleted folders with contents
    os.remove("C:\\Users\\Ignacy\\Desktop\\copy.txt")
except FileNotFoundError:
    print("That file was not found...")
except PermissionError:
    print("You do not have permission do delete this file")
else:
    print("Copied path was deleted")
