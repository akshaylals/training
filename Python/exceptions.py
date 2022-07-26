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