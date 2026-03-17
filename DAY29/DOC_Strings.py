# Docs are the information about functions or something else this docs are not as same as the comments. Compiler
# doesnt ignore the docs infact it treats the docs as special info and stores in (doc) attribute 
# Rule : - doc string must be written immedietly after the defination of function or above of function body

def square(n):
    '''The function expects the integer input and returns the square of the number''' # this may look like comments but its not comment its the doc string implementation
    print(n**2)

square(5)
print(square.__doc__)  # can see the docs by this methode

