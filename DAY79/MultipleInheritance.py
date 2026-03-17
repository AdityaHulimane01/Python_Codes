# Parent class 1
class Employee:
    def __init__(self, name):
        # stores employee name
        self.name = name

    def show(self):
        # prints employee name
        print(f"The name of the employee is {self.name}")


# Parent class 2
class Dancer:
    def __init__(self, dance):
        # stores dance style
        self.dance = dance

    def show(self):
        # prints dance style
        print(f"The dance type is {self.dance}")


# Child class using Multiple Inheritance
# Order matters: Employee is first, then Dancer
class EmployeeDancer(Employee, Dancer):

    # constructor of child class
    def __init__(self, name, dance):

        # Instead of calling parent constructors,
        # we directly assign the attributes
        # (works but not the best practice)
        self.name = name
        self.dance = dance


# Creating object of EmployeeDancer
E1 = EmployeeDancer("Kartik", "Bhangda")

# Calling show() method
# Because Employee class is first in inheritance,
# Python will call Employee.show() due to MRO
E1.show()


# MRO = Method Resolution Order
# It shows the order in which Python searches for methods
print(EmployeeDancer.mro())