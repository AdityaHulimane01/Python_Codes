contries = ("India" , "Bangladesh" , "Russia" , "Dubai" , "England" , "Paris" , "Paris")
contries2 = ("Europe" , "Naigeria" , "Finland")
print(contries)   

# Methode of manupulating the tuple indirectly by type conversion
# temp = list(contries)
# temp.append("Pakistan")
# temp.pop(1)
# temp[1] = "America"
# contries = tuple(temp)
# print(contries)

# concatination of tuples
contries3 = contries + contries2
print(contries3)

countParis = contries.count("Paris")
print(countParis)

idx = contries.index("Paris",3,6)
print(idx)