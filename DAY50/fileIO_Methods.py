f = open('myfile.txt' , 'r')

while True:
    line = f.readline()  # readline methode is used to read the file line by line 
    print(line)
    if not line:
        break

f = open('myfile.txt' , 'w')
lines = ['line 1' , 'line 2' , 'line 3']
for line in lines:
     f.writelines(line + '\n')       # writline methode is used to write the content linewise into the file
f.close