arguments = input("Введите числа: ")
arguments_list = arguments.split(',')

arguments_tuple = tuple(arguments_list)
print(arguments_tuple)

def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi
    for arg in (first, ) + args:
    #     if arg < res and lo < arg < hi:
    #         res = arg
    # return max(res, lo)
        print(arg, "arg")


bounded_min(-5, arguments_tuple, lo=10, hi=14)
