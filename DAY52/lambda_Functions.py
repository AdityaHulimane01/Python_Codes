
# def square(x):   # This can be also written as below using lambda function
#     return x*X

square = lambda x: x * x  # This is very simple just learned it becouse it will be used by many peoples so that we dont confuse
cube = lambda x: x * x * x
avg = lambda x , y , z: (x+y+z)/3

def appl(fx , value):
    return 6 + fx(value)

print(square(5))
print(cube(5))
print(avg(3,4,5))

print(appl(cube , 2))  # methode 1  (passing the cube function as an argument to the appl function. Yes we can do this! )
print(appl(lambda x: x * x * x , 2))  # methode 2



# 1. only use it when you want to complete the logic in one sentence 
# 2. It is used when we want to pass the function as an argument to the another funtion
