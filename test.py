# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
# def fibonacci(x):
#     if x < 2: return 1
#     return (fibonacci(x - 2) + fibonacci(x - 1))
#
#
# def factorial(x):
#     if x < 2: return 1
#     return (x * factorial(x - 1))
#
#
# def main():
#     funcs = [fibonacci, factorial]
#     n = 10
#     for i in range(len(funcs)):
#         print(funcs[i](n))
#
#
# main()
