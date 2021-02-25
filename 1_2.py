'''2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

time = int(input('Введите количество секунд: '))

hour = time // 3600
minute = (time - (hour * 3600)) // 60
second = time - (hour * 3600) - (minute * 60)

if hour < 10:
    hors = str(0) + str(hour)

if minute < 10:
    minute = str(0) + str(minute)

if second < 10:
    sek = str(0) + str(second)

print(f'{hour}:{minute}:{second}')