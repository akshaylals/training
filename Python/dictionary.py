# Dictionary
# method 1
myStudents = {'Abhi': 30, 'Sibi': 28, 'Subi': 'not updated'}
# method 2
myStudents = dict(Abhi=30, Sibi=28, Subi='not updated')
# method 3
myStudents = dict({'Abhi': 30, 'Sibi': 28, 'Subi': 'not updated'})
print(myStudents)

print(myStudents['Abhi'])

# Dictionary methods
print(myStudents.get('Abhi'))
print(myStudents.items())
print(myStudents.keys())
print(myStudents.values())

print(len(myStudents))
print('Abhi' in myStudents)         # check if key is present
print(30 in myStudents.values())    # check if value is present

myStudents2 = {'Abhi': 31, 'Binu':26}
print(myStudents, myStudents2)
myStudents.update(myStudents2)  # join together dict by overwritting duplicates
print(myStudents)

myStudents.clear()  # clear all values
print(myStudents)
del myStudents      # delete the dict along with the values
print(myStudents)
