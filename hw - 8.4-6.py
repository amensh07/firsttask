class Store:
    def __init__(self):
        print('Добро пожаловать на склад!')


class StockTec:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_unit = {'Модель': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} по цене {self.price} в наличии в количестве  {self.quantity}'

    def new_tec(self):
        # while True:
        #     if input("Для выхода из программы 'Q', "
        #              "для продолжения ввода элементов в список нажмите 'Enter'"):
        #         break
        try:
            # unit_name = input(f'Введите наименование ')
            # unit_price = int(input(f'Введите цену за ед '))
            # unit_qua = int(input(f'Введите количество '))
            # unique = {'Модель устройства': unit_name, 'Цена за ед': unit_price, 'Количество': unit_qua}
            # self.my_unit.update(unique)
            # #self.my_store.append(self.my_unit)
            return f'В наличии оргтехника -\n {self.my_unit}'
        except ValueError:
            return f' Проверьте тип данных '


class Printer(StockTec):
    def print(self):
        return f'Вы хотите напечатать на модели {self.name} ?'


class Scanner(StockTec):
    def scan(self):
        return f'Вы хотите отсканировать на модели {self.name} ?'


class Copier(StockTec):
    def copy(self):
        return f'Скопируйте файлы с модели {self.name} перед перезагрузкой!'

unit_1 = Printer('hp', 2000, 5)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Copier('Xerox', 1500, 1)
print(unit_1.new_tec())
print(unit_2.new_tec())
print(unit_3.new_tec())
print(unit_1.print())
print(unit_3.copy())
print(unit_2.scan())