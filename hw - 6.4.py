import random


class Car:
    def metod1(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def metod_go(self):
        return f'{self.name} поехала'

    def metod_stop(self):
        return f'{self.name} остановилась'

    def metod_turn(self):
        i = random.randint(0, 1)
        if i == 1:
            return f'{self.name} повернула направо'
        else:
            return f'{self.name} повернула налево'

    def show_speed(self):
        return f'{self.name} имеет скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            return 'Ваша скорость превышает допустимый максимум.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return 'Ваша скорость превышает допустимый максимум.'


class SportCar(Car):
    def sport(self, speed, color, name, is_police):
        super().metod1(speed, color, name, is_police)


class PoliceCar(Car):
    def police(self, speed, color, name, is_police):
        super().metod1(speed, color, name, is_police)


tesla = SportCar()
tesla.metod1(200, 'черный', 'Tesla 2020', False)
niva = TownCar()
niva.metod1(60, 'Белый', 'Niva', False)
lada = WorkCar()
lada.metod1(90, 'Голубой', 'Lada', True)
ford = PoliceCar()
ford.metod1(90, 'Зеленый', 'Ford Foxus', True)
cars = [tesla, niva, lada, ford]
for i in range(0, 4):
    print(cars[i].metod_go())
    print(cars[i].metod_turn())
    print((cars[i].show_speed()))
    print(cars[i].metod_stop())
    print(f'Is {cars[i].name} a police car? {cars[i].is_police}')
