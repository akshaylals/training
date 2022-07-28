import os

os.chdir(os.path.dirname(__file__))# Exception handling in python


# try, except, finally blocks (clause)
try:
    div = 4 // 2
    print(div)
except ZeroDivisionError:
    print('Attempting to divide by zero')
except:
    print('Some other exception occured')
else:
    # else will work if the try statements are successful
    print('Division completed and result is', div)
finally:
    print('This is code of finally clause')


# get the exception
try:
    div = 4 // 0
    print(div)
except Exception as e:
    # get the exception name
    print(f'{type(e).__name__} was occured. More details below.') 
    print(e)    # Print the entire details of the exception
finally:
    print('This is code of finally clause')


# Exception handling file
try:
    f = open('nonexistingfile.txt')
    try:
        f.write('Hello, World!')
    except:
        print('Some error writing to file')
    finally:
        f.close()
except:
    print('The file cannot be opened')


x = 0
try:
    if x == 0:
        raise Exception('Number cannot be zero')
except Exception as e:
    print('Error occured:', type(e).__name__, e)


y = 'foo'

try:
    if type(y) is not int:
        raise TypeError('Not an int')
except Exception as e:
    print('Error occured:', type(e).__name__, e)


# Create user-defined Exception class
class MyError(Exception):
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return repr(self.value)


try:
    x = 0
    if x == 0:
        raise MyError('The number is Zero !!')
except Exception as e:
    print(type(e).__name__, e)


# Exception derrived class being inherited by another class
class MyError(Exception):
    pass


class DivideByZero(MyError):
    pass


try:
    x = 0
    if x == 0:
        raise DivideByZero
except DivideByZero:
    print('Divide by zero')


