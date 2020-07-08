class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        var1 = self.v / 6.5 + 0.5
        return var1

    def suit(self):
        var2 = self.h / 6.5 + 0.5
        return var2

    @property
    def my_method(self):
        return f"Площадь ткани для пальто и костюма соответственно:" \
               f" {self.v / 6.5 + 0.5}, {self.h / 6.5 + 0.5}. " \
               f"Общая площадь ткани = {self.v / 6.5 + 0.5}+{self.h / 6.5 + 0.5} "


class Woman(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        print(f'Площадь ткани для пальто {self.v / 6.5 + 0.5}')


class Man(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        print(f'Площадь ткани для костюма {self.h / 6.5 + 0.5}')


wooman = Woman(46, 180)
print(wooman.my_method)
