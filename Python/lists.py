studentsAge = [18, 21, 23, 20, 21]
print(studentsAge)
print(studentsAge[2])
print(studentsAge[2:4])
print(studentsAge[1:5:2])
print(studentsAge[:3])
print(studentsAge[::-1])
print(studentsAge[-3])


studentsAge.append(16)
studentsAge.append('hi')
print(studentsAge)

del studentsAge[-1]
print(studentsAge)

# combine list using extend()
studentsName = ['Anu', 'Sinu', 'Binu']
studentsAge.extend(studentsName)
print(studentsAge)

# to check if an element is in the list using the 'in' operatior
print('Anu' in studentsName)
print('Anushka' in studentsName)

# get the length of the list
print(len(studentsName))

# reverse the contents of the list destructively
studentsName.reverse()
print(studentsName)

# sort a list
studentsName.sort()
print(studentsName)

# list concatnation
print(studentsName + studentsName)

# list duplication/multiplication usign * operator
print(studentsName * 3)

