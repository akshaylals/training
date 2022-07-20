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

# Time
import time
print(time.time()) # seconds past 1st Jan 1970
print(time.localtime(time.time()))  # get the multiple time values as a tuple
print(time.asctime(time.localtime(time.time())))    # get the time as string from a tuple

# for i in range(10):
#     print(i)
#     time.sleep(1)   # delay the program execution by the specified no of seconds.

import datetime 
print(datetime.datetime.now())

mydate = datetime.datetime(2020, 5, 4)
print(mydate)
mydate = datetime.datetime(2020, 5, 4, 10, 15, 40)
print(mydate)

# time comparison demo
from datetime import datetime as dt
if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
    print('Working hours.....')
else:
    print('shift complete')

import calendar
# get calendar for a month
myCalendar = calendar.month(2022, 5)
print(myCalendar)
# get calendar for a year
myCalendar = calendar.prcal(2022)
print(myCalendar)

