a = input("Enter any value between 5 and 9 : ")

if a == "quit":
    print("Done")

elif a.isdigit() and (int(a) < 5 or int(a) > 9):
    raise ValueError("Value must be between 5 and 9")

elif not a.isdigit():
    print("Invalid input, please enter a number between 5 and 9 or 'quit'.")

else:
    print("Valid input:", a)
