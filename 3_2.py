'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''

def user(name, surname, year, city, email, phone):
    return name, surname, year, city, email, phone

print(user(name='Ivan', surname='Ivanov', year=1990, city='Tambov', email='user@mail.com', phone=777))