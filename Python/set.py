# unordered 
# method 1
months = {'January', 'February', 'March', 'April'}
# mehtod 2
months = set(['January', 'February', 'March', 'April'])
print(months)
print(type(months))

# looping through elements in set using for loop
for month in months:
    print(month)

# declare an empty set
days = set()
# add values to set
days.add('Mon') # insert single item
days.add('Tue')
days.add('Wed')
print(days)

# insert multiple items
days.update(['Thu', 'Fri'])
print(days)

# remove items from the set
# using discard() method. Will remove item and not display item doesn't exist
days.discard('Thu')
print(days)
# using remove(). It will give error if item does not exist
days.remove('Fri')
print(days)

# clear the elements in the set
days.clear()
print(days)

# delete the set
del days
# print(days)

# set operations
# union, intersection, difference, symmetric difference

months1 = set(['January', 'February', 'March'])
months2 = set(['February', 'March', 'April', 'May'])
months3 = set(['November', 'February', 'December', 'March'])

# union
months4 = months1 | months2
print(months4)

# intersection
months4 = months1 & months2
print(months4)

# months1.intersection_update(months2, months3)
# print(months1)

# difference
months4 = months1 - months2
print(months4)

# symmetric difference
# common items removed 
months1 = set(['January', 'February', 'March', 'April'])
months2 = set(['March', 'April', 'April'])
months4 = months1 ^ months2
print(months4)
# another method
months4 = months1.symmetric_difference(months2)
print(months4)
# updates months1
months1.symmetric_difference_update(months2)
print(months1)

# set comparisons
days1 = {'Monday', 'Tuesday', 'Wednesday', 'Thursday'}
days2 = {'Monday', 'Tuesday'}
days3 = {'Monday', 'Tuesday', 'Friday'}
days4 = {'Monday', 'Tuesday', 'Friday'}

# checking if months1 is a superset of months2
print(days1 > days2)
print(days1 < days2)
# check if two sets are equal (no of elements and elements itself should be same)
print(days1 == days2)
print(days3 == days4)
# check if two sets are equal as well as days3 is a superset of days4
print(days3 >= days4)
# check if two sets are equal as well as days3 is a subset of days4
print(days3 <= days4)

# frozen set
fs = frozenset([1, 2, 3, 4, 5]) # immutable set
print(type(fs))
print(fs)

# fs.add(6)