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
    for item in range(len(l1), 0, -1):  # створення ренжом зворотньої індексації
        new_list.append(item)
    print(new_list)


# rev_for([1, 2, 3, 4, 5])


# def rev_for2(rev_list):
#     for item in range(len(rev_list)):
#
#     # print(rev_list)
#
#
# rev_for2([1, 2, 3, 4, 5])
