'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.'''

f_obj = open('5_4.txt', 'r', encoding='utf8')

f_obj2 = open('5_40.txt', 'w', encoding='utf8')

for i in f_obj:
    x = i.split()
    print(x)
    if x[0] == 'One':
        f_obj2.writelines('Один - ' + x[2])
    if x[0] == 'Two':
        f_obj2.writelines('\nДва - ' + x[2])
    if x[0] == 'Three':
        f_obj2.writelines('\nТри - ' + x[2])
    if x[0] == 'Four':
        f_obj2.writelines('\nЧетыре - ' + x[2])


f_obj.close()
f_obj2.close()
