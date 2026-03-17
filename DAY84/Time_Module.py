import time

# Function to calculate time taken by FOR loop
def for_loop_time(n):
    start = time.time()      # starting time

    for i in range(n):
        pass                 # empty operation just for timing

    end = time.time()        # ending time

    total = end - start      # time taken by for loop
    print("Time taken by FOR loop:", total, "seconds")


# Function to calculate time taken by WHILE loop
def while_loop_time(n):
    start = time.time()      # starting time

    i = 0
    while i < n:
        i += 1

    end = time.time()        # ending time

    total = end - start      # time taken by while loop
    print("Time taken by WHILE loop:", total, "seconds")


# Number of iterations
n = 10000000


print("Loop timing program\n")

# Calling the functions
for_loop_time(n)
while_loop_time(n)


# -----------------------------
# Using other time module functions
# -----------------------------

# Get current local time
current_time = time.localtime()
print("\nLocal Time object:", current_time)

# Convert it to readable format
formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", current_time)
print("Formatted Time:", formatted_time)

# Demonstrating sleep
print("\nProgram will pause for 2 seconds...")
time.sleep(2)
print("Program resumed after sleep.")