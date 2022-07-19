# Try except
try:
    answer = 12 / 0
    print(answer)
except:
    print('error')

try:
    answer = 12 / 0
    print(answer)
except ZeroDivisionError:
    print("divide by zero!")