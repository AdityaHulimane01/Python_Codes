# Local variables are the variables that are defined inside the function and cannot use or print it outside of the function
# Global variables are the variables that can be used in whole code at anywhere its value is available for each and every method

x = 10            # Global Variable

def func():
    # global x
    # x = 12
    y = 5         # Local Variable
    print(y)

func()
print(x)
print(y)   # This will throw error becouse y is the local var and it is not accessible outside of function


# but we can change the scope global varaiable inside the function, if you want to see uncomment the (gobal x) in line 7 and 8