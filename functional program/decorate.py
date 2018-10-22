import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print '2018-09-18'


# f = now
# f()
# print f.__name__


# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log('execute')
# def now():
#     print '2018-09-18'


# now()
# print now, now.__name__


class LogPlus:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print 'start call {}'.format(self.func.__name__)
        self.func(*args, **kwargs)
        print 'end call {}'.format(self.func.__name__)


@LogPlus
def hello():
    print '2017-11-06'


hello()
print hello
