# Higher Order fns
# reduce(), map(), filter()

# A higher-order fn printGreeting() takes two arguments:
# a fn f and a name n, and returns the result of calling f(n)
def greet(name):
    return 'Hello, {}!'.format(name)

def printGreeting(f, n):
    print(f(n))

printGreeting(greet, 'Abhi')

# Map fn
def myMapFn(a):
    return a * a

x = map(myMapFn, (1, 2, 3, 4, 5))
print(tuple(x))

# A simple program to input numbers and power and print powers
print('\n'.join(tuple(map(lambda a, p = int(input('Enter power: ')): f'{a} ^ {p} = {int(a) ** p}', input('Enter list of numbers: ').split()))))



# Filter fn
def func(x):
    if x >= 3:
        return x

y = filter(func, (1, 2, 3, 4))
print(list(y))

print(list(filter(lambda x: x >= 3, (1, 2, 3, 4))))


# Reduce fn
from functools import reduce
x = reduce(lambda a, b: a + b, [23, 21, 45, 98])
print(x)

# sum numbers between a range from input
print('Sum:', reduce(lambda a, b: a + b, filter(lambda x: 3 < x < 9, map(int, input('Enter numbers: ').split()))))

