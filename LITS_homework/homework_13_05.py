# 1. В рядку замінити пробіли зіркою. Якщо зустрічається підряд кілька пробілів, то їх слід замінити одним знаком "*", пробіли на початку і кінці рядка видалити.
# 2. Даний рядок, що містить натуральні числа і слова. Необхідно сформувати список з чисел, що містяться в цьому рядку. Наприклад, заданий рядок "abc83 cde7 1 b 24". На виході ми повинні отримати список [83, 7, 1, 24].
# 3. Визначити довжину найкоротшого слова в рядку.
# 4. Вводиться рядок. Необхідно визначити в ньому відсоток великих і малих букв.


# 1)
def stars_and_spaces():
    print(input("Введіть довільний рядок: ").strip().replace(" ", "*"))


# stars_and_spaces()


# 2)
def numbers_and_letters():
    string = input("Введіть довільний рядок: ")
    list_of_digits = []
    for i in string:
        if i.isnumeric():
            list_of_digits.append(i)
    print(list_of_digits)


# numbers_and_letters()


# 3)
def the_shortest():
    words_list = input("Введіть довільний рядок: ").split()
    print(words_list)
    # print(min(words_list).__len__())
    # shortest = min(words_list)
    # print(shortest.__len__())
    for word in words_list:
        result = word.count(word)
        if word.count(word) < result and word.isspace() != True:
            result = word.count(word)
    print("Довжина найкоротшого слова: ", result)


# the_shortest()


# 4)
def percent():
    big = 0
    small = 0
    string = input("Введіть довільний рядок: ")
    for word in string:
        if word.isupper() and word.isspace() != True:
            big += 1
        elif word.islower() and word.isspace() != True:
            small += 1
    print("Відсоток великих букв = ", (big/(big + small)) * 100, "%")
    print("Відсоток малих букв = ", (small / (big + small)) * 100, "%")


percent()
