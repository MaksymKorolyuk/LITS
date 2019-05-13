def minimal(numbers_func):
    def inner():
        numbers_func()
        print("something")
    return inner


@minimal
def numbers():
    string = input("Enter your string: ")
    list_of_numbers = []
    for number in string:
        if number.isdigit():
            list_of_numbers.append(number)
    print(list_of_numbers)
    return list_of_numbers


numbers()
