__author__ = 'joseph'


def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t


print(fibonacci(5))


# Fib with tuple unpacking
def fibonacci2(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y


print(fibonacci2(5))