staff1 = {
    1 : 45,
    2 : 78,
    3 : 33,
    4 : 89,
    5 : 30
}

staff2 = {
    222 : 98,
    386 : 69
}

# staff1.update(staff2)   for updating the staff1 dictionary
# print(staff1)

# staff1.clear()    used to clear the existing dictionary not for deleting the dictionary itself
# print(staff1)

# staff1.pop(4)   # used to remove a specific key value pair from the dictionary and returns the updated dictionary 
# print(staff1)    # if key value is not found it raises a KeyError

# staff1.popitem()   # used to remove the last inserted key value pair from the dictionary
# print(staff1)

# del staff1    # used to delete the dictionary itself

# del staff1[2]   # used to delete a specific key value pair from the dictionary and does not return anything
# print(staff1)   # if key value is not found it raises a KeyError

# print(staff1.get(3))   # used to get the value of a specific key    

# print(staff1.keys())   # used to get all the keys of the dictionary

# print(staff1.values())   # used to get all the values of the dictionary

# print(staff1.items())   # used to get all the key value pairs of the dictionary as tuples in a list 

# staff3 = staff1.copy()   # used to create a shallow copy of the dictionary
# print("This is copy of the staff1",staff3)  

# print(staff1.setdefault(6, 100))   # used to set a default value for a specific key if the key is not already present in the dictionary
# print(staff1)

# print(staff1.fromkeys(['a', 'b', 'c'], 0))   # used to create a new dictionary with the specified keys and a default value


