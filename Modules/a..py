from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3,4, 5, 6, 7, 7]
# sentence = 'blah blah thinking about python'
# print(Counter(li))
# print(Counter(sentence))

# dictionary = defaultdict(lambda: 'does not exit', {'a': 1, 'b': 2})
# print(dictionary['a'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)
