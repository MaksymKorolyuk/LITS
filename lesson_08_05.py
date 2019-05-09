# декораторы
# пример синтаксиса декоратора


# def dec(func):
#     def wrapper():
#         print("something")
#         func()
#         print("once more something")
#     return wrapper
#
#
# @dec
# def func():
#     print("inner function")
#
#
# func()
# -----------------------------------------

# def mul2(func):
#     def inner(*args):
#         r = func(*args)
#         return r * 2
#     return inner
#
# @mul2
# def f(a, b):
#     return a + b
#
#
# print(f(3, 3))
# --------------------------------------------

# def mul(a):
#     def inner(b):
#         return a * b
#     return inner
#
#
# mul2 = mul(2)
# print(mul2(2))
# ----------------------------------------------
# count = 0
#
#
# def counter(f):
#
#     def inner(*args, **kwargs):
#         global count
#         count += 1
#         f(*args, **kwargs)
#         inner.count = count  # аттрибут кaунт, который ссылаеться на счетчик count
#     return inner
#
#
# @counter
# def p():
#     print("Hallo")
#
#
# p()
# p()
# p()
# print(p.count)
# ------------------------------------------------

# def pr(func):
#     def inner(*args):
#         print("Values: ", args)
#         a = func(*args)
#         return a
#     return inner
#
#
# @pr
# def f(*args):
#     print("Actions: ", args)
#
#
# f(2, 3, 4, 5)
# --------------------------------------------------

def is_b_zero(func):
    def inner(a, b):
        if b == 0:
            print("b should not = 0")
        else:
            c = func(a, b)
            return c
    return inner


@is_b_zero
def f(a, b):
    print(a / b)


f(4, 1)
