class Employee:
    def __init__(self , name , Id):
        self.name = name
        self.Id = Id

    def EmpDetails(self):
        print(f"The name of Employee:{self.Id} is {self.name}")

class Programmer(Employee):     # Employee class is inherited by the Programmer means Extended
    def ProDetails(self):
        print(f"The Employee {self.name} is programmer")

E1 = Employee("Aditya" , 1)
E1.EmpDetails()
E2 = Employee("Suraj" , 2)
E2.EmpDetails()

E3 = Programmer("Yash" , 3) 
E3.EmpDetails()   # Here object of class Programmer can also use the methode of the class Employee by using the inheritance
E3.ProDetails()