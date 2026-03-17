class demo:
    def __init__(self, num):
      self.num = num
      print(self.num)

    def addNum(self,n):
       self.num = self.num+n
       print(self.num)
       
    @staticmethod
    def add(a,b):      #  static methode is created so that the user can access that perticular methode for the any arguments. 
      return a+b         # and also the class variables can also use this methode
       
a = demo(6)
a.addNum(5)
print(a.add(5,6))   # can also call like -->   print(demo.add(5,6)) 