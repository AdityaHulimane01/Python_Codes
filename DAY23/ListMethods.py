lst = [42,22,4,7,42]
print(lst)

# writting all the methods we can check it by uncommenting the perticular methode

# lst.append(8)
# lst.sort()
# lst.sort(reverse=True)  # sorts the list in descending order
# lst.reverse()  # Reverse the whole list
# lst.index(3)
# lst.count(42)

'''
m = lst.copy()  # used to assign the copy of one list into another 
m[0] = 0
print(m)
'''

# lst.insert(1,67)    # Inserts 67 at index 1

m = [12 , 4788, 87]   # new list
# lst.extend(m)         # take elements of m list and add it to the last indexes of the lst list

#  by using extend our lst list is changing but if we want that our lst list wont be changed we can de this
k = lst + m  # k is list holds data of both lists lst and m.
print(k)