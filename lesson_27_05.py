# classes


class D:
    l = []

    def __init__(self, l):
        self.l.extend(l)


d1 = D([1, ])
d2 = D([2, ])


# print(D.l)


class S:
    @staticmethod
    def static():
        print("staticmethod")


# S.static()


class Class_Method:
    @classmethod
    def cls_method(cls):
        print(cls.__name__)


# Class_Method.cls_method()


class Property_dec:
    @property
    def prop(self):
        return 1 + 1


# p = Property_dec()
# print(p.prop)


# створити клас "прямокутник", який буде мати два атрибути(сторони). об"єкти повинні мати два атрибути площу, периметр
# використати property i staticmethod


class Rectangle:
    def __init__(self):
        self.a = int(input("Side a: "))
        self.b = int(input("Side b: "))

    @property
    def sqr_per(self):
        sqr = self.a * self.b
        per = 2 * self.a + 2 * self.b
        return sqr, per

    @staticmethod
    def printed_sides(sqr, per):
        print("square and perimetr: ", sqr, per)


rect = Rectangle()
print(rect.sqr_per)
Rectangle.printed_sides(*rect.sqr_per)
