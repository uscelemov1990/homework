'''5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

f_obj = open('5_5.txt', 'w')

my_count = input('Введите числа: ').split()

for i in my_count:
    f_obj.writelines(i + '\n')

f_obj.close()


f_obj_2 = open('5_5.txt', 'r')

my_list = []

for i in f_obj_2:
    my_list.append(int(i))

print(sum(my_list))

f_obj_2.close()