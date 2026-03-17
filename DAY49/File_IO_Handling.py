# there are some methods for handling the files
#  1. read(r)     only used to read the content inside the file it throws error if the file does not exists

#  2. write(w)    used for write content inside the file. If file not exists then it creats the new file not throws error
#                 but if used for existing file the previous all data will vanish and new data will be stored 

#  3. append(a)   used to add the content in the existing file. this also creates the file if it not exists without throwing any error
#  
# 4. create(x)    used to create the file and throws the error if the file already exists

#  5. text(t)     used to handle the text file in text mode

#  6. binary(b)   used to handle the binary files (images , pdfs , etc)


# 1. READING THE FILE 
file = open('myfile1.txt' , 'r')    # Methode for opening the file for reading
content = file.read()
print(content)
file.close()       # methode for closing the file and it is necessary to close the file after procedure

# 2. WRITING THE FILE
file2 = open('myfile2.txt' , 'w')
file2.write("Hii this is happened too")   # change the content here and you will see the changes in myfile2.txt
file2.close()

# 3. APPEND IN THE FILE
file3 = open('myfile3.txt' ,'a')
file3.write("Yes the content is added") 
file3.close()

# 4. CREATING THE FILE
file4 = open('myfile4.txt' , 'x')  # try it by changing the file name and it will automatically get created dont create existing file otherwise it will throw the error





