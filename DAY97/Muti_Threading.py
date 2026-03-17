import threading
import time

# Normal function -> will run sequentially unless we use threads
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)   # blocks this function for given seconds


# ------------------- NORMAL EXECUTION -------------------
# Calls happen one by one (serial execution)

func(4)   # waits 4 sec
func(2)   # then waits 2 sec
func(1)   # then waits 1 sec

print()

# Total time ≈ 4 + 2 + 1 = 7 seconds 😴


# ------------------- SMART EXECUTION (THREADING) -------------------

# Creating threads -> each thread will run func() independently
t1 = threading.Thread(target=func , args=[4])
t2 = threading.Thread(target=func , args=[2])
t3 = threading.Thread(target=func , args=[1])

# start() -> actually starts the thread execution
t1.start()
t2.start()
t3.start()

# Important note:
# Threads run in parallel (kind of simultaneously)

# Total time ≈ max(4,2,1) = 4 seconds 🚀


# (Optional but important in real use)
# join() -> wait for all threads to finish before moving ahead

# t1.join()
# t2.join()
# t3.join()