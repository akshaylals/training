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
x = re.findall(r'[a-m]', txt)
print(x)

txt = 'James bond is 007'
x = re.findall(r'[0-9]', txt)
print(x)

x = re.findall(r'J...s', txt)
print(x)

x = re.findall(r'J[a-z]*s', txt)
print(x)

# look if the string starts with bond
x = re.findall(r'^James', txt)
print(x)
x = re.findall(r'\AJames', txt)
print(x)

# look if the string ends with bond
x = re.findall(r'007$', txt)
print(x)

# look if the word starts with bond
x = re.findall(r'\bbond', txt)
print(x)

# matching an email
txt = 'hello test@gmail.com how are you?'
# check for non space chars before and after '@'
x = re.findall(r'\S+@\S+', txt)
print(x)

