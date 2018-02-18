import time

def factorial_iterative(n):
    f = 1
    while n>0:
        f = f * n
        n -= 1
    return f
#Factorial here is done iteratively.

#To do this recursively

def factorial_recursive(n):
    if n < 2:
        return 1
    return n * factorial_recursive(n-1)

times = 10000
factorial_value = 900
before_time = time.time()
for _ in range(times):
    factorial_iterative(factorial_value)
print(f'This is how long the iterative took for {factorial_value}, {times} times', time.time()-before_time)

before_time = time.time()
for _ in range(times):
    factorial_recursive(factorial_value)
print(f'This is how long the recursive took for {factorial_value}, {times} times', time.time()-before_time)

