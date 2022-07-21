class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayEmpCount(self):
        print('Total no of employees:', Employee.empCount)
    
    def displayEmployeeDetails(self):
        print('Name:', self.name)
        print('Salary:', self.salary)


e1 = Employee('superman', 15000)
e1.displayEmpCount()
e1.displayEmployeeDetails()

e2 = Employee('spiderman', 17000)
e2.displayEmpCount()
e2.displayEmployeeDetails()

# Inheritance
# base class
class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def launch(self):
        return '%s has reached %s' % (self.name, self.distance)


class MarsRover(Rocket):
    def __init__(self, name, distance, maker, vehicleCode):
        Rocket.__init__(self, name, distance)
        self.maker = maker
        self.__vehicleCode = vehicleCode
    
    def get_maker(self):
        return '%s launched by %s' % (self.name, self.maker)
    
    def get_vehicleCode(self):
        return self.__vehicleCode


x = Rocket('simple rocket', 'till stratosphere')
y = MarsRover('mars_rover', 'till mars', 'ISRO', 1234)

print(x.launch())
print(y.launch())
print(y.get_maker())
print(y.get_vehicleCode())

# cannot access __vehicleCode
# print(y.__vehicleCode)
# can access variable __vehicleCode
# print(y._MarsRover__vehicleCode)


# Encapsulation
class Person:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    def display(self):
        print(self.__name)
        print(self.__age)
    

person = Person('Dev', 30)
person.display()

# cannot access
# print(person.__name)
# print(person.__age)

# can access
# print(person._Person__name)
# print(person._Person__age)


# Polymorphism
from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self):
        return 'I am a two dimensional shape.'

    def __str__(self) -> str:
        return self.name


class Square(Shape):
    def __init__(self, length) -> None:
        super().__init__('Square')
        self.length = length
    
    def area(self):
        return self.length ** 2
    
    def fact(self):
        return 'Squares have each angle equal to 90 degrees.'
    

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__('Circle')
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2


a = Square(4)
b = Circle(7)

print(b)
print(b.fact())
print(a.fact())
print(b.area())