import re
string = 'search this inside of this text please!'
pattern = re.compile('search this inside of this text please!')
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)