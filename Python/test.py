import sys
print(sys.version)
print('Hello, World!')

# % formatting
make = 'Dell'
dollarRate = 70.256
myText = 'the amount for this %s computer is %d USD and the exchange rate is %4.2f USD to 1 INR' %(make, 1299, dollarRate)
print(myText)

# Formatting using format() method
myText = 'The amount for this {} computer is {} USD and the exchange rate is {} USD to 1 INR'.format(make, 1299, dollarRate)
print(myText)

myText = '{0} is easier than {1}'.format('Python', 'Java')
print(myText)

# count the entire string 
print('Hello Good Morning'.count('d'))

# count from index 3 to end of string
print('Hello Good Morning'.count('d', 3))

# count from index 3 to 10-1
print('Hello Good Morning'.count('d', 3, 13))

myString = 'superman'
print("endswith('man')", myString.endswith('man'))
print("endswith('man', 3)", myString.endswith('man', 3))
print("endswith('man', 2, 6)", myString.endswith('man', 2, 6))
print("endswith(('man', 'ma'), 2, 6)", myString.endswith(('man', 'ma'), 2, 6))
print("endswith(('man', 'ma'), 2, 6)", 'Postman'.endswith(('man', 'ma'), 2, 6))

print('Hello Good Morning'.find('Go'))
print('Hello Good Morning'.find('Go', 4))
print('Hello Good Morning'.find('Go', 4, 15))
print('Hello Good Morning'.find('kk'))
# print('Hello Good Morning'.index('kk'))

print('isalnum()', 'hello1234'.isalnum())
print('isalnum()', 'h e l l o 1 2 3 4'.isalnum())

print("'hello'.islower()", 'hello'.islower())
print("'Hello World'.istitle()", 'Hello World'.istitle())
print("'HELLO'.isupper()", 'HELLO'.isupper())
