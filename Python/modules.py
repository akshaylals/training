# import random
# print(random.randrange(1, 10))

# import random as r
# print(r.randrange(1, 10))

from random import randrange
print(randrange(1, 10))

import random 
print(random.random())
print(random.randint(5, 20))
print(random.choice(['head', 'tail']))

myShirtColors = ['Blue', 'Red', 'Black', 'Yellow', 'Green']
random.shuffle(myShirtColors)
print(myShirtColors)

random.seed(1000)
print(random.random())