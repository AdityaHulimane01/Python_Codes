
#         Person
#        /     \
#    Student   Teacher


# Parent class
class Person:
    def __init__(self, name):
        # attribute of Person class
        self.name = name

    def showName(self):
        # method to display name
        print(f"Name: {self.name}")


# Child class 1
class Student(Person):
    def __init__(self, name, roll_no):
        # calling constructor of Person class
        super().__init__(name)
        # attribute of Student class
        self.roll_no = roll_no

    def showRoll(self):
        # method to display roll number
        print(f"Roll Number: {self.roll_no}")


# Child class 2
class Teacher(Person):
    def __init__(self, name, subject):
        # calling constructor of Person class
        super().__init__(name)
        # attribute of Teacher class
        self.subject = subject

    def showSubject(self):
        # method to display subject
        print(f"Subject: {self.subject}")


# Creating objects
s1 = Student("Kartik", 101)
t1 = Teacher("Rahul", "Math")

# Accessing methods
s1.showName()
s1.showRoll()

t1.showName()
t1.showSubject()