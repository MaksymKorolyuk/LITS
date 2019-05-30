# Написати клас, елементи якого буду себе поводити як стек(така структура данних).
# Використовувати тільки те, що було сьогодні на занятті.
# *Підсказка: придивіться до такого типу данних у пайтоні як список.
# Уточнення, стек має мати такий функціонал як добавляння, видалення у стек, провірку чи він порожній та мати атрибут, який містить глибину стека


class Stack:
    stack_list = [1, 2]

    def __init__(self):
        self.element = input("Enter new element: ")

    def insert_element(self):
        Stack.stack_list.append(self.element)
        return Stack.stack_list

    @staticmethod
    def delete_element():
        deleted = Stack.stack_list.pop()
        return deleted

    @staticmethod
    def empty_stack():
        if Stack.stack_list:
            print("Not empty", "Deep of stack: " + str(len(Stack.stack_list)), sep="\n")
        else:
            print("Empty")


new = Stack()
print(new.insert_element())
# print(Stack.delete_element())
Stack.empty_stack()
