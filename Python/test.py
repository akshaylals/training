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
print(myString.endswith('man'))
print(myString.endswith('man', 3))
print(myString.endswith('man', 2, 6))
print(myString.endswith(('man', 'ma'), 2, 6))
print('Postman'.endswith(('man', 'ma'), 2, 6))

print('Hello Good Morning'.find('Go'))
print('Hello Good Morning'.find('Go', 4))
print('Hello Good Morning'.find('Go', 4, 15))
print('Hello Good Morning'.find('kk'))
print('Hello Good Morning'.index('kk'))