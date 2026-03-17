# types of the arguments

# Type 1 : Required Arguments
'''
def average(a,b):
    print("The average is :",(a+b)/2)  
average(4,5) 
'''

# Type 2 : Default Arguments
'''
def average(a = 9,b = 5):   # here 9,5 are the default args means if any args not passed at the time of calling then this will used for calculation.
    print("The average is :",(a+b)/2)  
average()  # if any argument is given at the time of function call then it will ignore default args and use the given args
'''

# Type 3 : Keyword Arguments
'''
def average(a = 9,b = 5):
    print("The average is :",(a+b)/2)  
average(b = 12, a = 22)  # no need to worry about the sequece if used like this
'''

'''
def average(*numbers):  # works as tuple 
    sum = 0
    for i in numbers:
     sum += i
    return sum/len(numbers)

c = average(5 , 6 , 7 , 1)
print(c)
'''

def names(**name):   # works as dictionary
    print("Hey" , name["fname"] , name["mname"] , name["lname"])  # key words of dictionary(fname , mname , lname)
    

names(lname = "Hulimane" , mname = "Sanjay" , fname = "Aditya") # values for the keywords
