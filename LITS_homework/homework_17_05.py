# 1) написати дві функції сортування списку. Перша - сортування методом бульбашки, друга - методом вставки
# 2) Напишіть функцію, яка приймає текст (стрінг), а повертає словник, у якому ключі будуть окремі слова, а значенням - їхня кількість у тексті.

# 1)
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        print("Iteration: ", i)
        for j in range(len(lst) - i - 1):
            print(" j iteration: ", j)
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            # print(lst)
            # input()
    return lst


# print(bubble_sort([5, 1, 4, 2, 9, 8, 3, 7, 6]))


def insertion(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = key
    return data


# print(insertion([5, 1, 4, 2, 9, 8, 3, 7, 6]))


def count_elemts(lst):
    s = set(lst)
    j = 0
    for j in s:
        j += 1
    print(j)
    res = [0] * j
    for i in lst:
        res[i] += 1
    print(res)


# count_elemts([0, 2, 3, 4, 2, 1, 2, 4, 5, 1, 2, 0, 6, 6, 6])
# ---------------------------------------------------------
# 2)


def str_to_dict(string):
    keys = tuple(string.split(" "))
    res_dict = {}
    for i in range(len(keys)):
        res_dict.update({keys[i]: len(keys[i])})
    return res_dict


print(str_to_dict("shdgfgh jsfgjhs jsdfg sdhfgjh sfg"))
