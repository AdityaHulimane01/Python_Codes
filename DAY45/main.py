# Here in the harry.py the function (welcome) is created and called at the end 
# the problem is that if we import the file in this code it automatically executes the function hence
# The function prints the message 2 times. one that is called in the harry.py file and another that is called in the main.py file
# to resolve this this we use the statement that is present in the harry.py file


import harry

harry.welcome()