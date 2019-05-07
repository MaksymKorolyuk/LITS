# Завдання 2.1. Написати функцію, яка буде рахувати площу трикутника за трьома сторонами.
# Завдання 2.2. Написати функцію, яка буде провіряти існування трикутника за трьома сторонами, тобто повертати True або False.
# Завдання 2.3. Написати функцію, яка буде провіряти рік на високостність.
import math


# 2.1)
def square(*args):
    p = (args[0] + args[1] + args[2]) / 2
    s = math.sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
    print("Площа трикутника: " + str(s))


square(3, 4, 5)


# 2.2)
def existance(*args):
    if args[0] + args[1] > args[2] and args[1] + args[2] > args[0] and args[0] + args[2] > args[1]:
        return True
    else:
        return False


print(existance(3, 4, 5))
