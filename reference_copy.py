# -*- coding: utf-8 -*-

my_dict = {'a': [1, 2, 3, 4, 5], 'b': 2}

x = my_dict['a']
for i in range(5):
    x[i] = 0
print(my_dict['a'])

y = my_dict['b']
y = y + 1
print y
print my_dict['b']
