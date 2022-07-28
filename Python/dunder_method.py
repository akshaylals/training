print(dir(int))

a = 5
print(a.__class__)


class Foo:
    def __init__(self, val) -> None:
        self.val = val
    
    def __eq__(self, __o: object) -> bool:
        return __o.val == self.val
    
    def __add__(self, __o: object) -> object:
        return Foo(self.val + __o.val)
    
    def __str__(self) -> str:
        return str(self.val)


x = Foo(2)
y = Foo(5)
z = x + y

print(x == y)
print(z)


class Matrix:
    def __init__(self, m, n, a) -> None:
        if len(a) != m:
            raise Exception('Matrix rows do not match')
        for i in a:
            if len(i) != n:
                raise Exception('Matrix columns do not match')
        self.__m = m
        self.__n = n
        self.__matrix = a
    
    def __add__(self, __o: object) -> object:
        t = []
        if self.__m == __o.__m and self.__n == __o.__n:
            for x, y in zip(self.__matrix, __o.__matrix):
                tt = []
                for a, b in zip(x, y):
                    tt.append(a + b)
                t.append(tt)
        return Matrix(self.__m, self.__n, t)
    
    def __str__(self) -> str:
        return '\n'.join(['  '.join([str(j) for j in i]) for i in self.__matrix])

a = Matrix(2, 2, [[1, 2], [3, 4]])
b = Matrix(2, 2, [[5, 6], [7, 8]])

print(a + b)


class Car:
    def __str__(self) -> str:
        return f'{self.__class__.__qualname__}'


car = Car()
print(car)

class RandomNumbers:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __add__(self, other):
        if not isinstance(other, RandomNumbers):
            return NotImplemented
        return RandomNumbers(self.a + other.a, self.b + other.b)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__qualname__} ({self.a}, {self.b})'

set_a = RandomNumbers(2, 4)
set_b = RandomNumbers(3, 5)

print(set_a + set_b)

print('-' * 60)

# Demonstrating the class dunder methods
# Creating a class with an empty list of software names
# and an empty dict of software name and version as key value paris
class Softwares:
    names = []
    versions = {}

    def __init__(self, names) -> None:
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception('Names cannot be empty')
    
    def __str__(self):
        s = 'The list of softwares and its versions are:\n'
        for key, value in self.versions.items():
            s += f'{key}: {value}\n'
        return s
    
    def __setitem__(self, name, version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception('Software Name doesn\'t exist')
    
    def __getitem__(self, name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception('Software name doesn\'t exist')
    
    def __delitem__(self, name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception('Sw name doesn\'t exist')
    
    def __len__(self):
        return len(self.names)

    def __contains__(self, name):
        if name in self.versions:
            return True
        else:
            return False


sw1 = Softwares(['ps', 'msword', 'mspaint'])
sw1['msword'] = 2
print(sw1)

print(sw1['msword'])
print(len(sw1))

del sw1['msword']
print(sw1)
print(len(sw1))

print('foo' in sw1)
print('ps' in sw1)