'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

my_list = input('Введите несколко слов через пробел: ').split()

i = 1

while i <= len(my_list):
    print(str(i) + '. ' + my_list[i - 1][:10])
    i += 1

#2 вариант

for ind, el in enumerate(my_list):
    print(ind + 1, el[:10])