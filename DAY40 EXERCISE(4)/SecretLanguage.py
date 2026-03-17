import random
import string

# Encoding ------------>
# If the string is less than 3 simply reverse the string
# Else pop first letter of string and append it at last and then
# add 3 random letters at the front and last of the string

# Decoding ------------->
# Just do oppsite of Encoding

def random3():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

choice = input("What you want Encoding or Decoding ? : ")
output = []

if choice == "Encoding":
    msg = input("Enter the Message : ")
    lst = msg.split()      # list of words

    for word in lst:
        if len(word) <= 3:
            # reverse small words
            output.append(word[::-1])
        else:
            # shift
            shifted = word[1:] + word[0]
            # add 3 random letters at start and end
            final = random3() + shifted + random3()
            output.append(final)
    print()        
    print("Your Message is Successfully Encrypted")
    print(output)

if choice == "Decoding":
     msg = input("Enter the Message : ")
     lst = msg.split()      # list of words

     for word in lst:
        if len(word) <= 3:
            # reverse small words
            output.append(word[::-1])
        else:
            cleaned = word[3:-3]
            # shift
            original = cleaned[-1] + cleaned[:-1]
            # add 3 random letters at start and end
            output.append(original)
     print()       
     print("Your Message is Successfully Decoded")
     print(output)
