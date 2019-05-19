# collections, tuples
# list1 = [1, 2, 3]
# for item in list1[:]:
#     if item == 2:
#         list1.remove(2)
#     print(list1)


def rev_slice(l):
    l = l[::-1]
    print(l)


# rev_slice([1, 2, 3, 4, 5])


def rev_for(l1):
    new_list = []
    for i in range(len(l1), 0, -1):  # створення ренжом зворотньої індексації
        new_list.append(l1[i - 1])
    print(new_list)


# rev_for([1, 2, 3, 4, 8, 12])
