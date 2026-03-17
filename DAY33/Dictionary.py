# Dictionaries are the oredered collection of data items. 
# It can store the multiple items in the single variable.like (1 : "Harry")(Aditya : "Info" , "Address")

# Dictionary 1
dict = {
    1 : "Aditya",
    2 : "Suraj",
    3 : "Yash",
    4 : "Gaurav"
}

print(dict[4])
print()

for key in dict.keys():
    print(f"The value corresponding to the key {key} is {dict[key]}")


# Dictionary 2
info = {
    "name" : "Aditya",
    "Age" : 20,
    "Eligible" : "Yes"
}

print()
print(info)
print(info["name"])   # Methode 1    // throws error if the key not exists in the dictionary 
print(info.get("name"))   # Methode 2  // not throws the error and returns the none if key is not present

print()
print(info.items())

for key,values in info.items():
    print(f"The value corresponding to the key {key} is {values}")