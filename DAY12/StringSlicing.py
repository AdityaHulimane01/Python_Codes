name = "Aditya,Suraj,Yash"

print(name[0:6])  # 0 to 6 is written couse string slicing returns (n-1) strings 
print(len(name))  # we can fing length of the string by this

print(name[0:-14])  # This is valid 
print(name[-8:-14]) # this is not valid
print(name[-14:-8])  # But this is valid

nm = "Aditya"
print(nm[-4:-2])   