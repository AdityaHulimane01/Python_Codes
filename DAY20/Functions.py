def GeometricMeanCalculator(a,b):  # Function 1
    mean = (a*b)/(a+b)
    print(mean)

def checker(a,b):  # Function 2
    if(a>b):
        print("First value is greater than second value")
    else:
        print("Second value is greater than or equal to the first value")

def demo(a,b): # if we want to write Function logic after then we use (pass)
    pass


a = int(input("Enter the first value :"))
b = int(input("Enter the second value :"))

# Calling of the functions
checker(a,b)
GeometricMeanCalculator(a,b)