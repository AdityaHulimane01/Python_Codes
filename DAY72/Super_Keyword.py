class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

# class Programmer(Employee):
#     def __init__(self, name, id , lang):     # Insead of this we can use the superMethode to utilize the Employee class constructor. by this we can avoide the Redundant or repetative code 
#         self.name = name
#         self.id = id
#         self.lang = lang


class Programmer(Employee):
    def __init__(self, name, id , lang):
        super().__init__(name, id)
        self.lang = lang


Harry = Employee("Harry" , "101")
Rohan = Programmer("Rohan" , "402" , "Python")


# Super keyword is used to call the Pre-Existing methods or Constructors in child classes  so that we can avoid the repetative coding.