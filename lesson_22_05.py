# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# *a, = filter(lambda x: x % 2, l1)
# print(a)


def func():
    """
    кількість рядків, які треба зчитати з термінала
    вертає відсортований массив ( спочатку цілі числа, потім доповнений дробовими числами)
    """
    n = int(input("How many lines: "))
    inputed_list = []
    integer_list = []
    float_list = []
    res = []
    for i in range(n):
        inputed_list.extend(input("Enter your string: ").split(" "))
    for j in range(len(inputed_list)):
        if "." in inputed_list[j] or "," in inputed_list[j]:
            float_list.append(float(inputed_list[j]))
            float_list.sort()
        else:
            integer_list.append(int(inputed_list[j]))
            integer_list.sort()
    res.extend(integer_list)
    res.extend(float_list)
    print(res)


func()
