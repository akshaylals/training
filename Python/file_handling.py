import os

os.chdir(os.path.dirname(__file__))

myfile = open('myfile.txt', 'r')
# print(myfile.read(10))
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())