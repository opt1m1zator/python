# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class DivisionByZero(Exception):
    @staticmethod
    def division_by_zero(division, divider):
        try:
            if divider == 0:
                raise DivisionByZero('Нельзя делить на ноль')
            else:
                print(division / divider)
        except DivisionByZero as MyError:
            print(MyError)


print('Введите число для деления')
inp_division = int(input())
print('Введите число на которое делить')
inp_divider = int(input())
DivisionByZero.division_by_zero(inp_division, inp_divider)
