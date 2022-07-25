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

# A simple program to input numbers and print squares
print('\n'.join(tuple(map(lambda a, p = int(input('Enter power: ')): f'{a} ^ {p} = {int(a) ** p}', input('Enter list of numbers: ').split()))))



# Filter fn
def func(x):
    if x >= 3:
        return x

y = filter(func, (1, 2, 3, 4))
print(list(y))