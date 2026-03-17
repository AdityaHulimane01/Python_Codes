# Base class (Level 1)
class Person:
    def __init__(self, name):
        # attribute of Person class
        self.name = name

    def showName(self):
        # method to display the name
        print(f"Name: {self.name}")


# Derived class from Person (Level 2)
class Employee(Person):
    def __init__(self, name, salary):
        # calling constructor of Person class
        super().__init__(name)
        # attribute of Employee class
        self.salary = salary

    def showSalary(self):
        # method to display salary
        print(f"Salary: {self.salary}")


# Derived class from Employee (Level 3)
# This is multilevel inheritance: Person → Employee → Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        # calling constructor of Employee class
        super().__init__(name, salary)
        # attribute of Manager class
        self.department = department

    def showDepartment(self):
        # method to display department
        print(f"Department: {self.department}")


# Creating object of Manager class
m1 = Manager("Kartik", 50000, "IT")

# Manager can access methods of all parent classes
m1.showName()        # method from Person class
m1.showSalary()      # method from Employee class
m1.showDepartment()  # method from Manager class