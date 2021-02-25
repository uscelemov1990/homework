'''4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте
цикл while и арифметические операции.'''

number = int(input('Введите число: '))
count = 0
num = number

while num > 0:
    digit = num % 10
    if digit > count:
        count = digit
    num = num // 10

print(count)