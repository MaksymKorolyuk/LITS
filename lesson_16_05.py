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
    d3 = {}
    s1 = set(d1)
    s2 = set(d2)
    s3 = tuple(set(tuple(s1.intersection(s2)) + tuple(s1) + tuple(s2)))
    for i in s3:
        if i in d1 and i in d2:
            d3.update({i: d1[i] + d2[i]})
        elif i in d1:
            d3.update({i: d1[i]})
        elif i in d2:
            d3.update({i: d2[i]})
    return d3


print(merge({1: 11, 2: 22, 3: 33}, {1: 44, 2: 22, 5: 55, 6: 66}))
