import re

txt = 'bits of paper bits of paper'
x = re.search('bi', txt)
print(x)

print(x.span())
print(x.string)
print(x.group())

x = re.findall('bi', txt)
print(x)

x = re.split(' ', txt)
print(x)

x = re.sub(' ', '-', txt)
print(x)

txt = 'Hello world'
x = re.findall('[a-m]', txt)
print(x)

txt = 'James bond is 007'
x = re.findall('[0-9]', txt)
print(x)