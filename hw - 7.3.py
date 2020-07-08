class Cell:
    def __init__(self, qua):
        self.qua = int(qua)

    def __str__(self):
        return f'Всего клеток {self.qua * "*"}'

    def __add__(self, other):
        return Cell(self.qua + int(other.qua))

    def __sub__(self, other):
        return int(self.qua - int(other.qua)) \
            if (self.qua - other.qua) > 0 else print('При делении получается число меньше нуля!'
                                                     'Проверьте значения.')

    def __mul__(self, other):
        return Cell(int(self.qua * other.qua))

    def __truediv__(self, other):
        return Cell(round(self.qua // other.qua))

    def make_order(self, cell):
        row = ''
        for i in range(int(self.qua / cell)):
            row += f'{"*" * cell} \\n'
        row += f'{"*" * (self.qua % cell)}'
        return row


cells1 = Cell(11)
cells2 = Cell(66)
print(cells1.__str__())
print(cells2.make_order(4))
print(cells1.make_order(100))
