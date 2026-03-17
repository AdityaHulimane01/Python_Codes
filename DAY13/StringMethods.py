a = "Aditya"
b = "!!Yes!!!!!"
c = "Aditya!@#$%^&*()Aditya"
d = "hii iaM aditya"
e = "hii iaM aditya"
f = "Hii may name is Aditya. This is my codes"
g = "Aditya6714"
h = "Hiiamigo"
i = " "
j = "Journy To The West The Demon Strike Back"

print(a.upper())   # uppercase to check use methode [a.isupper()]
print(a.lower())   # lowercase to check use  [a.islower()]

# Since we used this two functions we may think that the original string was changed but its not like that (a = "Aditya") was
# never changed couse the Strings are Immutable and if we used any methodes on it , just the copy will be genrated it will not
# make any changes in original string.
print(a)

 # Removes the all ! from the string that is at the Ending of string it will not remove which are at the beggining of string
print(b.rstrip("!")) 

# Replace all occurence of perticular String with new one
print(c.replace("Aditya","Harry"))

# split methode will create the list of strings
print(d.split(" "))

# capitalize methode Turns the first letter of the string to the uppercase and if any other letter was remained 
# capital that was not supposed to be capital then it also turns it to lowercase, #works smart!.
print(e.capitalize())  # only works for single longest string.

# centre method alligns content to the centre but length of string increases due to addition of initial spaces occured by the 
# centre methode and this is only the copy it doesnt affect the original strings length
print(len(e))
print(e.center(100))
print(len(e.center(100)))

# count occurence of perticular string
print(c.count("Aditya"))

# Endswith methode checks if any string ends with the desired letter or not and returns (True or False)
# same for the startsWith methode
print(b.endswith("!"))
print(d.endswith("iaM",2,7))
print(b.startswith("A"))

# find returns the first occurence and returns index if found , if not found returns -1.
print(f.find("is"))

# isalnum returns true if the string is alphanumeric 
print(g.isalnum())

# returns true if string is only alphabetic. if space occured then also returns false
print(h.isalpha())

# isspace methode checks if the string only contains the space or not
print(i.isspace())

# title methode is used to turn the each strings first letter to upper case. also converts no needed uppercase letter to lowercase
print(d.title())

# istitle methode checks that is the first letter of each string is capital or not 
print(j.istitle())

# swapcase methode is used to swap the upper to lower case and vice versa
print(j.swapcase())


