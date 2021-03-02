'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

one = input('Введите первое число: ')
two = input('Введите второе число: ')

def division(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return ('Делить на 0 нельзя!')
    except ValueError:
        return 'Введите число'

print(division(one, two))