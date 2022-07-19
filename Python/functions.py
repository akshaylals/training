def findSum(a, b):
    sum = a + b
    return sum

print(findSum(2, 3))


def checkIfPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(checkIfPrime(7))
print(checkIfPrime(15))

def calculations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return (add, sub, mul, div)

output = calculations(49, 45)
print('Addition:', output[0])
print('Subtraction:', output[1])
print('Multiplication:', output[2])
print('Division:', output[3])

# yield
# converts normal python fn into a generator
def calculations(a, b):
    add = a + b
    yield add
    sub = a - b
    yield sub
    mul = a * b
    yield mul
    div = a / b
    yield div

for value in calculations(49, 45):
    print(value)
