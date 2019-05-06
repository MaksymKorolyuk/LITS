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


def fib(n):
    if n <= 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))
