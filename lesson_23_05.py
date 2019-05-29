# generators
# Завдання 1: Згенерувати матрицю розміром N*N де всі елементи будуть нулі
# Завдання 2: функція приймає число а повертає усі прості числа, що менші заданого


# 1)
def matrix():
    n = int(input("How many rows and columns should be in your matrix: "))
    zero = 0
    matrix_list = [zero for _ in range(n)]
    matrix_list = [matrix_list for _ in range(n)]
    print(matrix_list)


# matrix()

# 2)
def prime_list(i):
    primes_list = []
    if i == 0 or i == 1:
        print(i)
    else:
        primes_list = [n for n in range(2, i) if i % n == 0]
    print(primes_list)


prime_list(int(input("Enter your number: ")))
