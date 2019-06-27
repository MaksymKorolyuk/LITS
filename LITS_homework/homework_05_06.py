# Створити клас для римских цифр, який буде унаслідуватись від класу int.
# Класовий конструктор повинен приймати значення(аргумент, який приймеє чаислове значення у різних форматах)
# і параметер(ключове значення, тобто параметр за замовчуванням, який буде приймати у якому форматі ви передали значення у перший аргумет,
# тобто у бінарному, вісімковому, десятковому або шістнадцятковому).
# За допомогою магічних методів ви маєте забезпечити роботу математичних операторів (-,+,/,*,<,>,==, <=, >=, !=)
# при роботі екземплярів класу як з іншоми екземплярами цього класу, так і з цілими числами


class RomanNumber(int):
    @classmethod
    def roman_construct(cls, number, system=10):
        if system == 2:
            cls.number = str(number)
            cls.number = int(cls.number, 2)
            print(cls.number)
        elif system == 8:
            cls.number = str(number)
            cls.number = int(cls.number, 8)
            print(number)
        elif system == 16:
            cls.number = str(number)
            cls.number = int(cls.number, 16)
            print(number)


# roman_number = RomanNumber.roman_construct(1000, 2)
# print(RomanNumber.roman_construct(1000, 2))
RomanNumber.roman_construct(2322, 2)
