# some times in the flow of the code execution some error occurs. then the execution of the remaining code also terminates. 
# so for avoiding the termination remaining code and also handling the error we use the exception handling in the program
# It also avoids the system crashing when the unexpected errors occurs


a = input("Enter the number : ")
print(f"The multiplication table of the {a} is : ")



try:
   for i in range(1,11):
     print(f"{int(a)} x {i} = {int(a) * i}")
except:
   print("Invalid Input")



print()
print("Some line that will be only printed beacouse the usage of the try and except otherwise these lines will not be printed for the Invalid input only")
print("End of the program")

