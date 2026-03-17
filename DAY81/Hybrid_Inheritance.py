
#         Person
#        /     \
#    Student   Teacher
#         \     /
#         Assistant



# Base class
class Person:
    def __init__(self, name):
        # attribute of Person class
        self.name = name

    def showName(self):
        print(f"Name: {self.name}")


# First child class
class Student(Person):
    def __init__(self, name, roll):
        # calling constructor of Person
        super().__init__(name)
        self.roll = roll

    def showRoll(self):
        print(f"Roll Number: {self.roll}")


# Second child class
class Teacher(Person):
    def __init__(self, name, subject):
        # calling constructor of Person
        super().__init__(name)
        self.subject = subject

    def showSubject(self):
        print(f"Subject: {self.subject}")


# Hybrid class (Multiple inheritance)
class Assistant(Student, Teacher):
    def __init__(self, name, roll, subject):
        # calling Student constructor
        Student.__init__(self, name, roll)
        # calling Teacher constructor
        Teacher.__init__(self, name, subject)


# Creating object
a1 = Assistant("Kartik", 101, "Computer")

# Assistant can use methods from all classes
a1.showName()
a1.showRoll()
a1.showSubject()