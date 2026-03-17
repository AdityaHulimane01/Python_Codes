class Person:

    def __init__(self , name , occupation):
       self.name = name                        # Format =  self.variable = argument
       self.occupation = occupation

    def info(self):
        print(f"{self.name} is the {self.occupation}")


a = Person("Harry" , "Devloper")  # now you must think that the why self argument is not passed so 
# there is the catch that self argument automatically passes there is no need of the passing any value for it.
b = Person("Nitika" , "HR")

a.info()
b.info()
