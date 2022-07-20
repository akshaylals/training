def findSum(a, b):
    sum = a + b
    return sum

print(findSum(2, 3))


def checkIfPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(checkIfPrime(7))
print(checkIfPrime(15))

def calculations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return (add, sub, mul, div)

output = calculations(49, 45)
print('Addition:', output[0])
print('Subtraction:', output[1])
print('Multiplication:', output[2])
print('Division:', output[3])

# yield
# converts normal python fn into a generator
def calculations(a, b):
    add = a + b
    yield add
    sub = a - b
    yield sub
    mul = a * b
    yield mul
    div = a / b
    yield div

for value in calculations(49, 45):
    print(value)

# Variable scope
message1 = 'I am Global Variable'
def myFunction():
    global message1
    print('Inside the function')
    # Global variables are accessibel inside a fn
    print(message1)
    message2 = 'I am Local Variable'
    print(message2)
    message1 = 'Modifying the global variable'

myFunction()
print(message1)
# print(message2)


# Passing Arbitary List as Argument
def make_pizza(size, *toppings):
    print(f'Making a {size} - inch pizza with toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers')

# Required argument
def printme(str):
    print(str)

printme('test')
printme(str='test')

# Required argument
def printinfo(name, age):
    print(f'{name}, {age}')

printinfo('Tom', 10)
printinfo(age=10, name='Tom')

# optional keyword arguments
def printinfo(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

printinfo(age=10, name='Tom')


# Anonymous (Lambda) functions
sum = lambda arg1, arg2: arg1 + arg2
print('Value of total :', sum(10, 20))
print('Value of total :', sum(20, 20))


toIntList = lambda s: [int(i) for i in s.split()]
print(toIntList('1 2 3 4 5'))


###########################################
# Python functions as First class Objects #
###########################################

# Rights of a fn in python is similar to the
# rights of a variable
# 1) Assign a function to a variable
def myFunc1():
    print('This is myFunc1')

# Assigning function to variable
myMyFunction1 = myFunc1

myFunc1()       # call fn directly
myMyFunction1() # call fn via variable

print()
# 2) Pass a fn to another fn
def myFunc2(receivedFn):
    receivedFn()
    receivedFn()

myFunc2(myFunc1)

print()
# 3) Return a fn from another fn
def returnToUpper():
    return str.upper

toUpperFnRef = returnToUpper()
print(toUpperFnRef('hello world'))
print(returnToUpper()('hello'))


print()
# 4) Define a fn inside another fn
def outer():
    print('outer fn')

    def firstInner():
        print('first inner fn')

    def secondInner():
        print('second inner fn')
    
    firstInner()
    secondInner()

outer()


print()
# 5) Inner fn can access variables in the enclosing fn
def outer(myGreeting):
    print('outer fn says', myGreeting)

    def firstInner():
        print('inner fn says', myGreeting)
    return firstInner

innerFn = outer('Hello World')
innerFn()