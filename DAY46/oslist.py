import os

folders = os.listdir("data")
print(os.getcwd())
# os.chdir("/Users")
print(os.getcwd())


# After changing the directory the following code will not run 

# for folder in folders:   To see the how many folders are there
#     print(folder)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))  # to see that what is content inside the perticular folder

# os.system("pip install pandas")    # can run the commands of powershell or cmd 