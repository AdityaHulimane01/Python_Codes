# class Employee:
#     def __init__(self , name , salary):
#       self.name = name
#       self.salary = salary          # We were do this previously to use the constructor but we can also use the classMethods
                                      # as the constructors in python see below uncommented code .
# e = Employee("Harry" , 50000)
# print(e.name)
# print(e.salary)


class Employee:
     def __init__(self , name , salary):
      self.name = name
      self.salary = salary  

     @classmethod
     def fromStr(cls , str):
        return cls(str.split("-")[0] , str.split("-")[1])
    
str = "Harry-50000"
e = Employee.fromStr(str)
print(e.name , e.salary)

# Real Purpose of doing this stuff is ----->

# @classmethod is used to create an alternative constructor.
# It allows creating an object from a different input format (like string, file, dict, etc.)
# instead of passing parameters manually to __init__.
#
# cls refers to the class itself (Employee), so cls(...) calls the constructor.
#
# Example:
# "Harry-50000" → split into name and salary → creates Employee("Harry", 50000)
#
# Benefit:
# Cleaner code, reusable logic, and easier object creation from formatted data.