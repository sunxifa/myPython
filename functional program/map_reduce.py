# def f(x):
#     return x * x


# print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print [x * x for x in xrange(1, 10)]
# print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]
print [s.lower() if isinstance(s, str) else s for s in L]
# print [s.lower() if isinstance(s, str) else s for s in L]

# def add(x, y):
#     return x + y


# print reduce(add, [1, 3, 5, 7, 9])

# print reduce(lambda x, y: x + y, [1, 3, 5, 7, 9])

# print reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])


# def fn(x, y):
#     return x * 10 + y


# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


# print reduce(lambda x, y: x * 10 + y, map(char2num, '13579'))

# print reduce(fn, map(char2num, '13579'))


# def str2int(s):
#     # def fn(x, y):
#     #     return x * 10 + y

#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# print str2int('13579')


# print map(lambda x: x.title(), ['adam', 'LISA', 'barT'])
# print reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])


# print filter(lambda x: x % 2 == 0, xrange(10))
# print filter(None, xrange(10))
# def not_empty(s):
#     return s and s.strip()


# print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
