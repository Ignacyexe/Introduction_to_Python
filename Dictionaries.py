# dictionary - a changeable, unordered collection of unique key:value pairs
# fast because they use hashing, allow us to access a value quickly

capitals = {"Poland": "Warsaw",
            "USA": "Washington",
            "China": "Beijing",
            "Germany": "Berlin"}

capitals.update({"UK": "London"})   # this function will add key into dictionary
capitals.update({"USA": "New York"})   # this function will replace the value of existing key
capitals.pop("China")   # this function will remove the key value from dictionary
# capitals.clear()   # this function will clear the dictionary

# print(capitals["Poland"])
# ^ this is simple byt not safe solution, because incorrect key in dictionary will crash program

print(capitals.get("Mexico"))
print(capitals.keys())   # this function will print all the keys in dictionary
print(capitals.values())   # this function will print all the values within the key
print(capitals.items())   # this function will list out all the content of dictionary

for key, value in capitals.items():
    print(key, value)
