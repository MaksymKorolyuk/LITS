for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz " + str(i))
    elif i % 5 == 0:
        print("buzz " + str(i))
    elif i % 3 == 0:
        print("fizz " + str(i))
