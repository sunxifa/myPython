# -*- coding: utf-8 -*-
"""
   Python出于对性能的考虑，但凡是不可变对象，在同一个代码块中的对象，
   只有是值相同的对象，就不会重复创建，而是直接引用已经存在的对象。
"""
a = 4444
b = 4444

print a is b
print a == b
print id(a)
print id(b)
