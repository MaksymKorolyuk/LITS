# dictionaries and sets


def f(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    s3 = s1 & s2
    print(list(s3))


# f([1, 2, 3], [2, 3, 4])


def g(d, k, v=None):
    if k in d:
        return d[k]
    else:
        return v


# print(g({1: 'one', 2: 'two', 3: 'three'}, 4))


def merge(d1, d2):
    s1 = set(d1)
    s2 = set(d2)

    return s1


print(merge({1: 11, 2: 22, 3: 33}, {1: 44, 5: 55, 6: 66}))
