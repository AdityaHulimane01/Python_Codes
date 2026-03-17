# Set does not prints repeated values it as same like lists with some unique specs and is unordered

Set = {2 , 3 , 4 , 5 , 5}
print(Set)

info = {"Adi" , 8.9 , "India" , 44 , 100} # order is not maintained but cannot be accessed by the index of the Set
for val in info:
    print(val)

adi = {}     # Set and Dictionary both are defined by this same methode so compiler will assume it as dictinary even if you created the empty set here
print(type(adi))

# to avoid this use 
Adi = set()
print(type(Adi))