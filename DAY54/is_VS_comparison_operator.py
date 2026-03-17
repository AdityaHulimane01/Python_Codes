a = 6
b = 6

c = ["Harry"]
d = ["Harry"]

e = 4
f = "4"

g = (1 , 2)
h = (1 , 2)

 # (is) used for comparing the locations of the objects in the memory 
 #  (==) used for comparing the values directly

print(a is b)     # both are same
print(a == b)  
print()

print(c is d)    # lists are mutable and lists are allocted at different memory locations so this will be false
print(c == d)
print()

print(e is f)   # e is int and f is String so there is type mismatch so this (is) will be false
print(e == f)
print()

print(g is h)  # as tuples are immutable so they are allocated at same memory location
print(g == h)
print()

