# Print Fibonacci 1 1 2 3 5 8 13
import time
import sys
from functools import lru_cache

def fibonacci_recursive(number):
    if number < 2:
        return 1
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)

@lru_cache(maxsize=None)
def fibonacci_recursive_cached(number):
    if number < 2:
        return 1
    return fibonacci_recursive_cached(number - 1) + fibonacci_recursive_cached(number - 2)

cache = {} #This contains numbers and their corresponding fibonnaci summed value.

def fibonacci_memoized_recursive(number):
    if number < 2:
        return 1
    elif number in cache:
        return cache[number]
    sum = fibonacci_memoized_recursive(number - 1) + fibonacci_memoized_recursive(number - 2)
    cache[number] = sum
    return sum

# More Optimized Following:

def fibonacci_iterative(number):
    first_num = 1
    second_num = 0
    temp = 0
    for _ in range(number+1):
        temp = second_num
        second_num = first_num + second_num
        first_num = temp
    return second_num

sys.setrecursionlimit(2000)
times = 100
test_value = 2090

before_time = time.time()
for _ in range(times):
    fibonacci_iterative(test_value)
print(f'This is how long the fibonacci iterative took for {test_value}, {times} times', time.time() - before_time)

# before_time = time.time()
# for _ in range(times):
#     fibonacci_recursive(test_value)
# print(f'This is how long the fibonacci recursive took for {test_value}, {times} times', time.time() - before_time)

# before_time = time.time()
# for _ in range(times):
#     fibonacci_recursive_cached(test_value)
# print(f'This is how long the fibonacci recursive cached took for {test_value}, {times} times', time.time() - before_time)

# before_time = time.time()
# for _ in range(times):
#     fibonacci_memoized_recursive(test_value)
# print(f'This is how long the fibonacci memoized recursive took for {test_value}, {times} times', time.time() - before_time)