# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax


# print calc_sum(*range(10))


# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum


# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print f1
# print f1()
# print f1 == f2


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs


# f1, f2, f3 = count()
# print f1, f1()
# print f2, f2()
# print f3, f3()


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            # def g():
            #     return j * j
            # return g
            return lambda: j * j
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print f1, f1()
print f2, f2()
print f3, f3()
