def welcome():
    print("hey you are welcome from harry")

print(__name__)
if __name__ == "__main__":  # This can avoid that problem
 welcome()

                                                                                    
# Basically the fact is that if we importing the file or module and not used the [ __name__ == "main"  ]
# then the methods or the procedures in that file will automatically executed without asking the permission of user
# Imagine if the perticular function from another file is capable of deleting the os of your device then ??
# So it is good to use this for our protection also
