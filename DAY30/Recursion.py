# factorial calculation using the recursion
'''
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
'''

# Fibonacci seris using recursion

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibo(i), end=" ")
