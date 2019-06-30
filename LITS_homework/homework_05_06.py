# Створити клас для римских цифр, який буде унаслідуватись від класу int.
# Класовий конструктор повинен приймати значення(аргумент, який приймеє чаислове значення у різних форматах)
# і параметер(ключове значення, тобто параметр за замовчуванням,
# який буде приймати у якому форматі ви передали значення у перший аргумет,
# тобто у бінарному, вісімковому, десятковому або шістнадцятковому).
# За допомогою магічних методів ви маєте забезпечити роботу математичних операторів (-,+,/,*,<,>,==, <=, >=, !=)
# при роботі екземплярів класу як з іншоми екземплярами цього класу, так і з цілими числами


class RomanNumber(int):
    def __init__(self, number, system=10):
        self.number, self.system = str(number), system
        self.dec = int(self.number, self.system)

    def checkio(self):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self.dec // 1000]
        h = hunds[self.dec // 100 % 10]
        te = tens[self.dec // 10 % 10]
        o = ones[self.dec % 10]

        self.res = t + h + te + o
        return self.res

    def __str__(self):
        return str(self.checkio())


new_roman = RomanNumber('15', 10)
print(new_roman)
