class A:
    a = 'a'

    def print_self(self):
        print("A")


class B:
    b = 'b'

    def print_self(self):
        print("B")


class C(A, B):
    c = 'c'

    def print_self(self):
        print("CC")
        # super(B, self).print_self()


c = C()


# print(c.a, c.b, c.c)
# c.print_self()
# print(C.mro())  #  метод вказує спадковість классів
# print(type(c))  # повертає класс атрибуту

# print(dir(A))
# print(A.__dict__)


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


# декоратори классу
import functools


#
#
# def class_decorator(cls):  # аргумент приймає клас
#     @functools.wraps(cls)  # аргумент приймає клас
#     def inner(*args):    # повинен приймати всі аргументи, що __init__ класу
#         #  необхідно обов"язково створювати об"єкт классу, і передавати всі необхідні аргументи
#         obj = cls(*args)
#         print(obj)
#         return obj
#     return inner
#
#
# @class_decorator
# class Class_for_decorator:
#     # методи і атрибути класу


# def singletone(cls):
#     instance = None
#
#     def inner(*args, **kwargs):
#         nonlocal instance
#         if instance is None:
#             instance = cls(*args, **kwargs)
#         return instance
#
#     return inner
#
#
# @singletone
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(3, 4)
# p2 = Point(4, 5)
# print(p1 is p2)


# клас My_dict, який наслідується від dict, об'єкт dict'a має записуватися через магічний метод __iadd__ в My_dict

class Dict:
    def __init__(self, dict):
        self.dict = dict

    def __iadd__(self, other, new_res):
        self.dict.update(new_res)
        return other.dict


res = Dict({'key1': 'value1', 'key2': 'value2', })
new_res = {'key3': 'value3'}
print(res.__iadd__(res, new_res))
