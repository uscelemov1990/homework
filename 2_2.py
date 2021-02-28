'''2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''

my_list = input('Введите данные через пробел: ').split()
new_list = []

i = 0

if len(my_list) % 2 == 0:
    while i < len(my_list):
        new_list.append(my_list[i + 1])
        new_list.append(my_list[i])
        i += 2
else:
    n = my_list.pop()
    while i < len(my_list):
        new_list.append(my_list[i + 1])
        new_list.append(my_list[i])
        i += 2
    new_list.append(n)

print(new_list)