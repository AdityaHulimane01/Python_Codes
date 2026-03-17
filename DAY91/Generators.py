# Generator function -> like a factory that produces values ONE by ONE
def my_generator():
    # Loop that will generate numbers from 0 to 49999
    for i in range(50000):
        yield i   # yield = "pause here and give value", remember state for next call


# Creating the generator object
gen = my_generator()  
# Think of this as: engine started, but it won't run until we ask for values


# next() -> manually pull the first item from the generator
print(next(gen))  
# Output: 0
# Generator now pauses AFTER yielding 0


# If we uncomment these, it keeps pulling next values
# print(next(gen))  # would print 1
# print(next(gen))  # would print 2
# print(next(gen))  # would print 3


# Now we loop over the generator
for j in gen:
    print(j)
    # Important memory trigger:
    # The loop CONTINUES from where generator last paused
    # Since we already consumed 0 using next(), loop starts from 1