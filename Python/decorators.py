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

# Returning values from decorated fn
@myDecorator
def myFnToPass(myString, myString2):
    returnString = 'Passing into decorator and printing {} {}'.format(myString, myString2)
    return returnString

# Returns none
print(myFnToPass('hello', 'world'))

print('-' * 60)

# Returns the value
def myDecorator(myFunc):
    @functools.wraps(myFunc)
    def innerWrapper(*args):
        print('Before the fn call')
        value = myFunc(*args)
        print('After the fn call')
        return value

    return innerWrapper

@myDecorator
def myFnToPass(myString, myString2):
    returnString = 'Passing into decorator and printing {} {}'.format(myString, myString2)
    return returnString

# Returns the string
print(myFnToPass('hello', 'world'))

print('-' * 60)

def acceptDecorator(myString3):
    def myDecorator(myFunc):
        @functools.wraps(myFunc)
        def innerWrapper(*args):
            print('string from decorator', myString3)
            print('Before the fn call')
            value = myFunc(*args)
            print('After the fn call')
            return value

        return innerWrapper

    return myDecorator

@acceptDecorator('testing string into decorator')
def myFnToPass(myString, myString2):
    returnString = 'Passing into decorator and printing {} {}'.format(myString, myString2)
    return returnString

print(myFnToPass('hello', 'world'))

print('-' * 60)

# Decorator with classes
print('Decorator with classes')
print()

# Decorating methods of a class
# @classmethod and @staticmethod
class Hero:
    @classmethod
    def say_class_hello(cls):
        if (cls.__name__ == 'HeroSon'):
            print('Hi Prince')
        elif (cls.__name__ == 'HeroDaughter'):
            print('Hi Princess')
    
    @staticmethod
    def say_hello():
        print('Hello...')


class HeroSon(Hero):
    def say_son_hello(self):
        print('Hello Son!')


class HeroDaughter(Hero):
    def say_daughter_hello(self):
        print('Hello Daughter!')


son = HeroSon()
son.say_class_hello()
son.say_son_hello()
son.say_hello()

daughter = HeroDaughter()
daughter.say_class_hello()
daughter.say_daughter_hello()
daughter.say_hello()

print('-' * 60)

# @property
class House:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self.__price = new_price
        else:
            print('Please enter a valid price')

    @price.deleter
    def price(self):
        del self.__price


house = House(50000.0)
print(house.price)
house.price = 40000.0
print(house.price)
del house.price
# print(house.price)

print('-' * 60)

