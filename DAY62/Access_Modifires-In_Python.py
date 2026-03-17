# There are no dedicated access modifires in the python but some conventions are made to consider the perticular variable as private , protected , public


class Employee:
    def __init__(self):
        self.name = "Harry"
        self.__Id = 66       # This (__) is used to make the variable private and prevents the direct access. still it can be accessd

Emp1 = Employee()
print(Emp1.name)

# print(Emp1.__Id)   # This will throw error
print(Emp1._Employee__Id)   # By this methode we can still access the private variables indirectly its called the (Name Mangling)

# (_) for protected
# (__) for private
