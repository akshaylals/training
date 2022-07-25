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

print('-' * 60)

# Abstract Class
print('Abstract Class')
print('-' * 15)


class Lion:
    def give_food(self):
        print('Feeding a lion with raw meat!')
        

class Panda:
    def feed_animal(self):
        print('Feeding a panda with bamboo!')
        
        
class Snake:
    def feed_snake(self):
        print('Feeding a snake with mice!')


simba       = Lion()
kungfupanda = Panda()
kingcobra   = Snake()

simba.give_food()
kungfupanda.feed_animal()
kingcobra.feed_snake()

print('-' * 60)

# Abstract class
from abc import ABC, abstractmethod
# ABC is Abstract Base Class
# from abc module, we have to import ABC and decorator abstractmethod

class Animal(ABC):      # Inherit from ABC
    @abstractmethod     # Decorator to define abstract method
    def feed(self):
        pass


class Lion(Animal):
    def feed(self):
        print('Feeding a lion with raw meat!')
        

class Panda(Animal):
    def feed(self):
        print('Feeding a panda with bamboo!')
        
        
class Snake(Animal):
    def feed(self):
        print('Feeding a snake with mice!')


zoo = [Lion(), Panda(), Snake()]

for animal in zoo:
    animal.feed()

print('-' * 60)


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def do(self, action):   #action is abstract fn parameter
        pass


class Lion(Animal):
    def feed(self):
        print('Feeding a lion with raw meat!')
    
    def do(self, action, time):
        print('Doing', action, 'at', time)
        

class Panda(Animal):
    def feed(self):
        print('Feeding a panda with bamboo!')
    
    def do(self, action, time):
        print('Doing', action, 'at', time)
        
        
class Snake(Animal):
    def feed(self):
        print('Feeding a snake with mice!')
    
    def do(self, action, time):
        print('Doing', action, 'at', time)


zoo = [Lion(), Panda(), Snake()]

for animal in zoo:
    animal.feed()
    animal.do('feeding', '10:10AM')

print('-' * 60)

# Abstract property
class Animal(ABC):
    @property
    @abstractmethod
    def diet(self):
        pass

    @property
    def food_eaten(self):
        return self.__food
    
    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self.__food = food
        else:
            raise ValueError('this animal doesn\'t eat this')

    @abstractmethod
    def feed(self):
        pass


class Lion(Animal):
    @property
    def diet(self):
        return ['antelope', 'cheetah', 'buffalo']

    def feed(self):
        print(f'Feeding a lion with {self.food_eaten}!')
        

class Panda(Animal):
    @property
    def diet(self):
        return ['bamboo', 'leaves']

    def feed(self):
        print(f'Feeding a panda with {self.food_eaten}!')
        
        
class Snake(Animal):
    @property
    def diet(self):
        return ['mice', 'rabbit']

    def feed(self):
        print(f'Feeding a snake with {self.food_eaten}!')
        

simba       = Lion()
kungfupanda = Panda()
kingcobra   = Snake()

simba.food_eaten        = 'buffalo'
kungfupanda.food_eaten  = 'bamboo'
kingcobra.food_eaten    = 'mice'

for animal in [simba, kungfupanda, kingcobra]:
    animal.feed()