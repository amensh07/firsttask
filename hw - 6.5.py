class Stationery:
    def metod(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen()
pen.metod('карандашом Н1')
print(pen.draw())
pencil = Pencil()
pencil.metod('черной ручкой')
print(pencil.draw())
handle = Handle()
handle.metod('красным маркером')
print(handle.draw())
