marks = [12 , 56 , 32 , 98 , 12 , 25 , 1 , 4]
Fruits = ["Apple" , "Mango" , "Banana"]


# Methode 1 for finding the index of the element from the list

# index = 1
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("You are the topper")
#     index += 1


# Methode 2  using the Enumerate function 

# for index , mark in enumerate(marks,start=1):
#     print(mark)
#     if index == 3:
#         print("You are the topper")

# Enumerate function is the built in function in python that is that allows us to loop over the sequence 

for i , fruit in enumerate(Fruits,start=1):
    print(i , "." , fruit)