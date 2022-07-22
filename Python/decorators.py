# A decorator in Python is a fn that takes another 
# fn as an argument and extends its behavior wihtout 
# explicitly modifying it

# Syntax:
#   func = decorator(func)
# func is the fn being decorated,
# decorator is used to decorate it 

def myDecorator(myFunc):
    def innerWrapper():     # wrapper fn 'decorates' the fn recieved
        '''Doc string of inner wrapper'''
        print('Before the fn call')
        myFunc()
        print('After the fn call')
    
    return innerWrapper

# define fn to pass
def myFnToPass():
    print('Passing into the decorator and printing')

myDecoratorDemo = myDecorator(myFnToPass)
myDecoratorDemo()


print()

# decorating fn using @
@myDecorator
def fnToDecorate():
    '''This is a doc string tyo describe fnToDecorate fn'''
    print('fn decorated with @')

# returns name and docstring of wrapper fn
fnToDecorate()
print(fnToDecorate.__name__)
help(fnToDecorate)

print('-' * 60)
# keeping name and docstring of decorated fn

import functools
def myDecorator(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper():
        print('Before the fn call')
        myFunc()
        print('After the fn call')
    
    return innerWrapper

@myDecorator
def fnToDecorate():
    '''This is a doc string tyo describe fnToDecorate fn'''
    print('fn decorated with @')


fnToDecorate()
print(fnToDecorate.__name__)
help(fnToDecorate)

print('-' * 60)


# Passign arguments into decorators
def myDecorator(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(myString):
        print('Before the fn call')
        myFunc(myString)
        print('After the fn call')

    return innerWrapper
# only work with fn with exactly 1 arg
@myDecorator
def myFnToPass(myString):
    print('Passing into decorator and printing', myString)

myFnToPass('hello')

print('-' * 60)

# Passing variable no of arguments into decorators
def myDecorator(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        print('Before the fn call')
        myFunc(*args)
        print('After the fn call')

    return innerWrapper
    
# works with multiple no of args
@myDecorator
def myFnToPass(myString):
    print('Passing into decorator and printing', myString)

@myDecorator
def myFnToPass2(myString, myString2):
    print('Passing into decorator and printing', myString, myString2)

myFnToPass('hello')
print()
myFnToPass2('hello', 'world')

print('-' * 60)