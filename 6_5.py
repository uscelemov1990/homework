'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода
draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.'''

class Stationery():
    def __init__(self, my_title):
        self.my_title = my_title

    def draw(self):
        print(f'Запуск отрисовки: {self.my_title}')


class Pen(Stationery):
    def __init__(self, my_title='ручка'):
        self.my_title = my_title


class Pencil(Stationery):
    def __init__(self, my_title='карандаш'):
        self.my_title = my_title


class Handle(Stationery):
    def __init__(self, my_title='маркер'):
        self.my_title = my_title


my_pen = Pen()
my_pen.draw()

my_pen = Pencil()
my_pen.draw()

my_pen = Handle()
my_pen.draw()