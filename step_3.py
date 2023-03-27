# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class List:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        my_value = None
        while my_value != 'stop':
                my_value = input('Введите значение или stop для выхода')
                if my_value == 'stop':
                    print(f'Список - {self.my_list} \n ')
                    break
                else:
                    try:
                        my_value = int(my_value)
                        self.my_list.append(my_value)
                        print(f'Список - {self.my_list} \n ')
                    except:
                        print(f"Вы ввели неправильное значение. Можно вводить только числа или stop")
                        y_or_n = input(f'Ввести еще раз? Y/N ')
                        if y_or_n == 'Y' or y_or_n == 'y':
                            print(try_except.my_input())
                        else:
                            return f'Вы вышли'

try_except = List(None)
print(try_except.my_input())
