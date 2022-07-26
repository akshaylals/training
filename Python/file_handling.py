import os

os.chdir(os.path.dirname(__file__))

myFile = open('myfile.txt', 'r')
# print(myfile.read(10))
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())

# reading the contents of the file line by line using for loop
for line in myFile:
    print(line)

# we need to close the file cursor/obj once we completed
# the operation associated with it
myFile.close()

myFile = open('myfile.txt', 'r')
contentList = myFile.readlines()
print(contentList)
for i in contentList:
    print(i.strip())
myFile.close()

# Append mode
# myFile = open('myfile.txt', 'a')
# myFile.write('Humpty dumpty sat on a wall\n')
# myFile.close()


# Write mode
# content will be replaced with new content
# myFile = open('myfile.txt', 'w')
# myFile.write('Humpty dumpty sat on a wall\n')
# myFile.close()

print('-' * 60)

myFile = open('myfile.txt', 'r')
print(myFile.readline().strip())
print(myFile.readline().strip())
print(myFile.readline().strip())
print(myFile.tell())

# Change the file pointer offset using seek()
myFile.seek(20)
print(myFile.tell())
print(myFile.readline().strip())

myFile.close()

import os
# if os.path.exists('myfile.txt'):
#     os.rename('myfile.txt', 'myfilenew.txt')
#     print('The file has been renamed')
# else:
#     print('The file does not exist')

# if os.path.exists('myfile.txt'):
#     os.remove('myfile.txt')
#     print('The file has been removed')
# else:
#     print('The file does not exist')

# Create a new directory
# os.mkdir('mydir')

# print current working directory
# print(os.getcwd())

# change current working directory
# os.chdir('mydir')
# print(os.getcwd())

# go back to previous directory
# os.chdir('..')
# print(os.getcwd())

# delete the directory
# os.rmdir('mydir')

print(os.listdir('.'))


# run an external python file saving output as txt
import subprocess
with open('output.txt', 'wb') as f:
    subprocess.check_call(['python', 'hello.py'], stdout=f)