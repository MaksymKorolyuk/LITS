# Завдання 1. Перевернути число введене в консолі. Наприклад 1234 введено, а на виході 4321
# Завдання 2. Вводиться натуральне число (ціле більше нуля). Необхідно знайти суму і добуток цифр, з яких складається це число. При цьому якщо в числі зустрічається цифра 0, то її не треба враховувати при знаходженні добутка.
# Завдання 3. Визначити, скільки в числі парних цифр, а скільки непарних. Число вводиться з клавіатури.
# Завдання 4. Написати програму, яка виконує над двома числами одну з чотирьох арифметичних операцій (додавання, віднімання, множення або ділення). Програма повинна завершуватися тільки за бажанням користувача. (Операцію також потрібно зчитати)

# 1)
# num = str(int(input('Введіть Ваше число: ')))
#
# num_list = list(num)
# for i in range(len(num_list) - 1, -1, -1):
#     print(num_list[i])


# 2)
num = int(input('Введіть Ваше число: '))

while num < 0:
    print("Число повинно бути більше нуля!")
    num = int(input('Введіть Ваше число: '))

num_list = list(str(num))

if len(num_list) == 1:
    print("Сума та добуток дорівнюють: " + str(num_list[0]))
elif len(num_list) >= 2:
    result = int(num_list[0])
    mult_result = int(num_list[0])
    for i in range(1, len(num_list)):
        print("Iterator: " + str(i))
        print("Length: " + str(len(num_list)))
        print("Result on start: " + str(result))
        print("Number for this iteration: " + str(num_list[i]))
        result = result + int(num_list[i])
        print("Result of iteration: " + str(result) + "\n")

        if int(num_list[i]) == 0:
            num_list[i] = 1
        mult_result = mult_result * int(num_list[i])
    print("Сума: " + str(result))
    print("Добуток: " + str(mult_result))


# 3)
# number = str(int(input("Введіть Ваше число: ")))
# number_list = list(number)
# even = odd = 0
# for i in range(len(number_list)):
#     if int(number_list[i]) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Парні: " + str(even))
# print("Непарні: " + str(odd))


# 4)
# running = True
# while running:
#     number1 = float(input("Введіть перше число: "))
#     number2 = float(input("Введіть друге число: "))
#     op = input("Яку операцію здійснити?: ")
#     if op == "+":
#         summ = number1 + number2
#         print("Результат: " + str(summ))
#         cont = input("Продовжити?: ")
#         if cont == "Ні" or cont == "ні":
#             running = False
#             print("Завершення программи")
#         elif cont == "Так" or cont == "так":
#             continue
#     elif op == "-":
#         summ = number1 - number2
#         print("Результат: " + str(summ))
#         cont = input("Продовжити?: ")
#         if cont == "Ні" or cont == "ні":
#             running = False
#             print("Завершення программи")
#         elif cont == "Так" or cont == "так":
#             continue
#     elif op == "/":
#         summ = number1 / number2
#         print("Результат: " + str(summ))
#         cont = input("Продовжити?: ")
#         if cont == "Ні" or cont == "ні":
#             running = False
#             print("Завершення программи")
#         elif cont == "Так" or cont == "так":
#             continue
#     elif op == "*":
#         summ = number1 * number2
#         print("Результат: " + str(summ))
#         cont = input("Продовжити?: ")
#         if cont == "Ні" or cont == "ні":
#             running = False
#             print("Завершення программи")
#         elif cont == "Так" or cont == "так":
#             continue
#     else:
#         print("Введений неправильний символ операції! Повторіть!")
#         continue
