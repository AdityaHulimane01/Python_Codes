# fstring is used to fetch the name and other all details in some fixed phrase like used below

name = input("Enter your name : ")
Age = input("Enter age : ")
Address = input("Enter address : ")

Details = f"Hi my name is {name} and iam {Age} years old. I live at the {Address}"  # Implimentation of the fStrings
print(Details)

# output : - 
# Enter your name : Aditya
# Enter age : 20
# Enter address : Uruli Kanchan
# ------>Hi my name is Aditya and iam 20 years old. I live at the Uruli Kanchan

# the details of the phrase can be changed and fetched in the phrase as per the need like,

# Enter your name : suraj
# Enter age : 20
# Enter address : Varwand
# ----->Hi my name is suraj and iam 20 years old. I live at the Varwand