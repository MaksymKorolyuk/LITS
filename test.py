string = input("Enter your string: ")
list_of_numbers = []


def minimal(numbers_func):
    def inner():
        numbers_func()
        res = min(list_of_numbers)
        print(res)
    return inner


@minimal
def numbers():
    for number in string:
        if number.isdigit():
            list_of_numbers.append(number)
    print(list_of_numbers)


numbers()
