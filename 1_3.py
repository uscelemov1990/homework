'''3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

count = input('Введите число: ')

result = int(count) + int(count + count) + int(count + count + count)

print(result)