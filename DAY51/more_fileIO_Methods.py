with open('myfile.txt' , 'w') as f:
  
  f.write('hii this is the hello world program and you are the guest here')
  f.truncate(20)


with open('myfile.txt' , 'r') as f:

#   f.seek(12)        # skips the intitial 12 letters along with the spaces
#   print(f.tell())    # Tells us that how many characters or letters are seeked and the current position of the cursor
#   data = f.read(5)  # starts reading the 5 letters only, after the skipped letters
#   print(data)
    print(f.read())



  
