# Looping in python
# use for loop to loop/iterate through a list in python
fruits = ['apples', 'oranges', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Use for loop to generate a series of numbers 
# using the range function
for i in range(10):
    print(i)

# while loop
counter = 5
while counter > 0:
    print('Counter =', counter)
    counter -= 1

# Break statement
j = 0
for i in range(5):
    j = j + 2
    print('i =', i, ', j =', j)
    if j == 6:
        break

# Continue statement
j = 0 
for i in range(5):
    j = j + 2
    print('i =', i, ', j =', j)
    if j == 6:
        continue
    print('j value is', j)

