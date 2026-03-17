x = input("Enter your first number : ")    # we can also add text while taking input from user
y = input("Enter your second number : ")

print("The sum is :" , x+y) 

 # This will not add , instead it will concatinate the x and y becouse pythons input() function is not enough capable
 #  to differentiate the inputs according to data types it considers each input as the String input so we need to typecast them
 # to add them

print("The Sum is :" , int(x) + int(y))