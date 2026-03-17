from functools import lru_cache
import time

# lru_cache -> remembers results of previous function calls
# maxsize=None -> unlimited memory (store all results)
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)   # Simulating a heavy/slow computation (waits 5 seconds)
    return n*5      # Actual calculation


# First time calling -> takes 5 seconds (not in cache yet)
print(fx(20))
print("Done for 20")

# First time -> again takes 5 seconds
print(fx(2))
print("Done for 2")

# First time -> again takes 5 seconds
print(fx(6))
print("Done for 6")


# Now these values are already stored in cache memory
# So they will run instantly (no 5 second delay)

print(fx(20))   # returned from cache
print("Done for 20")

print(fx(2))    # returned from cache
print("Done for 2")

print(fx(6))    # returned from cache
print("Done for 6")


# New value -> not stored in cache yet
# So again it will take 5 seconds
print(fx(60))
print("Done for 60")