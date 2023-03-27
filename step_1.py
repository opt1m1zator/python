# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split("-"):
            date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 < year:
                    return f'Данные верны'
                else:
                    return f'Ошибка года'
            else:
                return f'Ошибка месяца'
        else:
            return f'Ошибка дня'

    def __str__(self):

        return f'Дата {Data.extract(self.day_month_year)}'


print('Проверка формата 16, 10, 2023', Data.valid(16, 10, 2023))
print('Проверка формата 16, 15, 2023', Data.valid(16, 15, 2023))
print('Проверка формата 40, 12, 2023', Data.valid(40, 12, 2023))
print('Проверка формата 16, 12, 0', Data.valid(16, 12, 0))
print('Конвертация даты из строки 22-01-2013', Data.extract('22-01-2013'))

