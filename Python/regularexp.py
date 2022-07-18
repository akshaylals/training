import re

txt = 'bits of paper bits of paper'
x = re.search('bi', txt)
print(x)

print(x.span())
print(x.string)
print(x.group())