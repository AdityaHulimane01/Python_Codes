tup = (3,4,5,"Aditya",True)    # Tuples are immutable and is written in the between of the two round braces
print(type(tup) , tup)

# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])

# tup[0] = 90  # this is not valid we cant insert couse tuples are immutable

if "Aditya" in tup:
    print("Yes element is present")
else:
    print("no")

# Slicing is possible in tuples but for results new tuple will be created in the memory and it will be returned
tup2 = tup[1:4]
print(tup2) 
