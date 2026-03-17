
# it is used to get the documentation of the object or class

print(help(str))

class Person:
    def __init__(self , name , ID):
        self.name = name
        self.ID = ID
        self.version = 1;

P = Person("Aditya" , 1)

print(help(Person))