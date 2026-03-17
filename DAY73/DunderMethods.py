class Employee:
    def __init__(self , name):
      self.name = name


    def __str__(self):        # Used to get the info about the object
       return f"The name of the Employee is {self.name}"
    
    def __repr__(self):       # if the str methode not found at the time of execution then the program executes the repr methode as the backup
       return f"Employee('{self.name}')"
    
    def __call__(self):     # it makes the object of the class direct callable 
       print("Hey this object is the callable becouse of the __call__ methode")
    

e = Employee("Harry")
print(str(e))      #  __str__ methode is used like this when calling for the object
print(repr(e))     #  __repr__ methode is used like this when calling for the object
e()              # This is the direct object methode call and its implimentaion is in __call__ methode