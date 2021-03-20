'''1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.'''

f_obj = open('5_1.txt', 'w')

my_text = []

while True:
    my_text_input = input()
    if my_text_input == '':
        break
    my_text.append(my_text_input)
    my_text.append('\n')

f_obj.writelines(my_text)

f_obj.close()