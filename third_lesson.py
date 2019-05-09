# def y(x):
#     y = x * x
#     print(y)
#
# y(9)


# def y(x):
#     if x < 0:
#         res = abs(x) / x
#     elif x == 0:
#         res = 0
#     elif x > 0:
#         res = x * x
#     print(res)
#
#
# y(-5)

# def fib(n):
#     """I make Fibonacci"""
#     if n <= 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(5))
# print(fib.__doc__)


# def printarg(first, *args):
#     print(args, sep=',')
#     print(type(args))
#     print(args[3])
#
#
# printarg()

xs = [1, 5, -7, 20]
print(min(*xs))




