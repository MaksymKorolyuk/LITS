# g = (x ** x for x in range(2))
# print(next(g))
# print(next(g))


# def fib(n):
#     a, b = 0, 1
#     while True:
#         if a <= n:
#             yield a
#             a, b = b, b + a
#         else:
#             break
#
#
# f = fib(1000)
# for i in f:
#     print(i)


# def chain(*iterable):
#     for it in iterable:
#         for item in it:
#             yield item
#
#
# for i in chain([1, 2, 3], {4: 4, 5: 5}):
#     print(i)


# def seq():
#     n = 0
#     while True:
#         yield n
#         n = 4 * n + 3
#
#
# m = 0
# for i in seq():
#     m += i


# def gen():
#     n = yield
#     while True:
#         yield n
#         n = 3*n + 3
#
#
# g = gen()
# print(g.send(None))
# print(g.send(1))
# for i in g:
#     print(i)
#     i += 1
#     if i >= 100:
#         raise StopIteration


# def cycle(*iterable):
#     for it in iterable:
#         for item in it:
#             yield item
#
#
# def infinite():
#     yield n
#
#
# for i in cycle(['a', 'b', 'c'], ['d', 'e']):
#     print(i)
