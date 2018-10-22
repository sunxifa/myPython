# def int2(x, base=2):
#     return int(x, base)


# print int2
# print int2('1000000')


import functools


int2 = functools.partial(int, base=2)
print int2('1000000')

kw = {'base': 2}
print int('1000000', **kw)
print int2('1000000', base=10)


max2 = functools.partial(max, 10)

print max2(1, 2, 3)

args = (1, 2, 3, 10)
print max(*args)
