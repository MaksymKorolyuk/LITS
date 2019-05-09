# строки
# one = 1
# two = 2
# print(f'{one} + {one} = {two}')  # f-string example
# print(r'\n Hello \n')  # "сырая" строчка для регулярных выражений
# print(dir('hello'))  # shows methods for this type
# ---------------------------------------------------------------


# def is_float(string):
#     if "." in string:
#         return True
#     else:
#         return False
#
#
# print(is_float(str(10.5)))
# ---------------------------------------------------------------


def add_new_line(func):
    def inner():
        print("\n", func(), "\n")
    return inner


@add_new_line
def max_input():
    numbers = input("Your numbers: ")
    numbers_int = numbers.split(' ')
    res = 0
    for i in numbers_int:
        if int(i) > res:
            res = int(i)
    return res


max_input()
# ---------------------------------------------------------------



