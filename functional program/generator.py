# g = (x * x for x in range(10))

# for n in g:
#     print n


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b = b, a + b
#         n += 1


# fib(6)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1


# print fib(6)
# for n in fib(6):
#     print n,

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3


o = odd()
print o.next()
print o.next()
print o.next()
print o.next()
