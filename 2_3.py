'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени
года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.'''

season = ['winter', 'spring', 'summer', 'autum']

month = int(input('Введите число месяца: '))

if month == 3 or month == 4 or month == 5:
    print(season[1])
elif month == 6 or month == 7 or month == 8:
    print(season[2])
elif month == 9 or month == 10 or month == 11:
    print(season[3])
elif month == 12 or month == 1 or month == 2:
    print(season[0])
else:
    print('Неверное число!')


season = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autum',
    10: 'autum',
    11: 'autum',
    12: 'winter'
    }

month = int(input('Введите число месяца: '))

if month >= 1 and month <= 12:
    print(season[month])
else:
    print('Неверное число!')