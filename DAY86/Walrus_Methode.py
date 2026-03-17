
# foods = list()
# while True:
#     food = input("What food you like : ")       # This is common methode but we can use better methide than this using the walrus operator
#     if food == "Quit":
#         break
#     foods.append(food)


foods = list()
while(food := input("What food you like : ") != "Quit"):   # This is better version with less code and more readibility. and (:=) this is walrus operator
    foods.append(food)

