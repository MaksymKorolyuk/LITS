# 1)за допомогою цикла while вивести всі парні числа в діапазоні 1-1000;
# 2)сгенерувати ряд Фібоначчі до 1000;

# 1)
i = 1
while i <= 1000:
    if i % 2 == 0:
        print(i)
    i += 1


# 2)
fib1 = 1
fib2 = 2
for i in range(1000):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib_sum)
