# Написати клас, елементи якого буду себе поводити як стек(така структура данних).
# Використовувати тільки те, що було сьогодні на занятті.
# *Підсказка: придивіться до такого типу данних у пайтоні як список.
# Уточнення, стек має мати такий функціонал як добавляння, видалення у стек, провірку чи він порожній та мати атрибут, який містить глибину стека


class Stack:
    stack_list = []

    def __init__(self):
        self.i = int(input("How many elements would you like to add to your stack: "))

    def insert_element(self):
        for j in range(self.i):
            j = input("Enter new element: ")
            Stack.stack_list.append(j)
        return Stack.stack_list

    @staticmethod
    def delete_element():
        deleted = Stack.stack_list.pop()
        return deleted

    @staticmethod
    def empty_stack():
        if Stack.stack_list:
            print("Not empty")
            print("Deep of stack: ", len(Stack.stack_list))
        else:
            print("Empty")

    @staticmethod
    def show_stack():
        print(Stack.stack_list)


new = Stack()
print(new.insert_element())
print("Deleted element: ", Stack.delete_element())
Stack.empty_stack()
new.show_stack()
