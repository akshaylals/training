# A decorator in Python is a fn that takes another 
# fn as an argument and extends its behavior wihtout 
# explicitly modifying it

# Syntax:
#   func = decorator(func)
# func is the fn being decorated,
# decorator is used to decorate it 

def myDecorator(myFunc):
    def innerWrapper():     # wrapper fn 'decorates' the fn recieved
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
    print('fn decorated with @')

fnToDecorate()