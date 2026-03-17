def ErrorHandling():
   
 try:
   array = [3 , 4 , 6 , 1]
   i = int(input("Enter the index : "))
   print(array[i])
   return 1         # even the return is used the code will execute the finally code block

 except IndexError:
   print("Invalid Index")
   return 0        # even the return is used the code will execute the finally code block

 finally:          # this code always runs even the code returns anything before this 
   print("Iam the code that always runs")


x = ErrorHandling()
print(x)