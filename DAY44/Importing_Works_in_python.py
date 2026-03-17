import math as m   # for importing all the math functions from the package

from math import sqrt as s , pi  # for importing the specific functions from the package

result = m.sqrt(9) * m.pi
print(result)
print(s.__name__)

print(dir(m))

from Hello import welcome , harry     # importing the functions and variables from the other files in same folder
welcome()
print(harry)