# -------------------->>>>>>>  MAP

l = [1 , 2 , 4 , 6 , 4 , 3]

# newList1 = []
# for item in l:                    # This is methode 1 it too long so mapping is used to easily manipulate the list elements
#     newList1.append(lambda x: x*x*x)
# print(newList1)

newList1 = list(map(lambda x: x*x*x,l))  # by defsult the map methode returns the map object even for list so we converts it back to the list using list methode
print(newList1)

# -------------------->>>>>>>  FILTER

newList2 = list(filter(lambda a: a>4 , l))  # The predefine function can be also passed as an argument to the map , filter .
print(newList2)

# -------------------->>>>>>>  REDUCE

from functools import reduce

numbers = [1 , 2 , 3 , 4 , 5]

sum = reduce(lambda x,y: x+y , numbers)
print(sum)



# Your confusion is basic but common. Here are the one line purposes. Read them carefully and stop mixing them up.

# map
# Transforms each element independently. Input list size equals output list size.

# filter
# Selects elements based on a condition. Output list size is less than or equal to input.

# reduce
# Combines all elements into a single value by repeatedly applying an operation.

# If you still think map and reduce are similar, you are wrong.
# map is one to one transformation.
# reduce is many to one aggregation.

# That is the difference.
