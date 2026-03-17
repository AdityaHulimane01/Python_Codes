''' for i in range(12):
    print("5 X" , i+1,"=",5*(i+1))
    if(i == 9 ):
        break  # It is used to break the loop when the i reached the value 9
'''

for i in range(12):
    if(i == 9 ):  # i starts from 0 so [9 is (10)]
       print("Skipping the calculation for 5 X",i+1,"=",5*(i+1))
       continue  # used to skip the iteration for the specific part of the code like iteration for 10 in output
    print("5 X" , i+1,"=",5*(i+1))  # This never runs for the 5 X 10 = 50
   
#  block of the code that is after the continue statement is never used for the specific part of the code that is mentioned by user
 