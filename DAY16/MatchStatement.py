# match statement is like the switch case methode used in the C and C++ programs

x = int(input("Enter your choice : "))

match x:        # matching the x with each case
    case 0:
        print("Your chosen number is 0")
    case 1:
        print("Your chosen number is 1")

    case _ if(x>90):                  # using (if) statement in the case statement
        print("choice is greater than 90")
    case _ if(x>80):
        print("choice is greater than 80")
    case _ if(x>70):
        print("choice is greater than 70")   # Always use in the decending order or as per need.
    case _ if(x>60):
        print("choice is greater than 60")
    case _ if(x>50):
        print("choice is greater than 50")
        
    case _:                          # if no case matches then this will be executed      
        print("Hey this is default case and your choice is :" , x)