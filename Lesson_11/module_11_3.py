import numpy
import inspect


def introspection_info(obj):
    info_obj = {}
    info_obj['type'] = type(obj)
    info_obj['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info_obj['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info_obj['module'] = inspect.getmodule(obj)
    if hasattr(obj, '__name__'):
        info_obj['name'] = obj.__name__
    if hasattr(obj, '__len__'):
        info_obj['length'] = len(obj)
    return info_obj


def sum_number(x=10):
    y = 11
    return x + y


class Exponentiation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def exponentiation(self):
        c = self.a ** self.b
        return c

exp = Exponentiation(5, 6)

res1 = introspection_info(numpy)
res2 = introspection_info(exp)
res3 = introspection_info('Hello Python')
res4 = introspection_info([15, 21, 33, 42])
res5 = introspection_info(sum)

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
