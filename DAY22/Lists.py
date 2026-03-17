marks = [3,5,6,"Aditya",True]  # list is a ordered collection of data
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print()

if 7 in marks:     # To check if element is present in list or not
    print("yes") 
else:
    print("No")

if "Aditya" in marks:     
    print("yes")
else:
    print("No")

# we can also use this methode for the strings
if "Adi" in "Aditya":
    print("yes !!")

# Slicing of list
print(marks)
print(marks[1:4])    # 1:4 means start from 1 and end at 4-1    eg-(1:4 is 1 to 3)
print(marks[1:4:2])   # here (2) means jump index that jumps on the indexes that are differ by 2

lst = [i*i for i in range(10)]  # This is called the List Comprehension
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)