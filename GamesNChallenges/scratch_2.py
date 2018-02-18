def factorial(n):
    f = 1
    while n>0:
        f = f * n
        n -= 1
    return f

print(factorial(23))
