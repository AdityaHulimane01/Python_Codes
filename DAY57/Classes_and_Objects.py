class Person:            
    name = "Harry"              # This are the default values but we can also pass our values 
    occupation = "Devloper"
    networth = 100000

    def info(self):     # This (self) is the default argument for every function
        print(f"{self.name} is the {self.occupation} with networth {self.networth}")

a = Person()    # Object 1 named (a)
b = Person()    # Object 2 named (b)

a.info()         # This will print the default values 

print()
a.name = "Aditya"
a.occupation = "Engineer"   # This are the values that will override the default values in the classes
a.networth = 10
a.info()  

b.name = "Nitika"
b.occupation = "HR"
b.networth = 0
b.info()


