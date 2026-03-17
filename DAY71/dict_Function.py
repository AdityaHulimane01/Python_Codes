class Person:
    def __init__(self , name , ID):
        self.name = name
        self.ID = ID
        self.version = 1;

P = Person("Aditya" , 1)

print(P.__dict__)