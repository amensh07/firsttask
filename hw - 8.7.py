class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел равна ComplexSum = {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        return f'Произведение комплексных чисел равно ComplexMul = ' \
               f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * j'


z_1 = Complex(1, -2)
z_2 = Complex(3, 4)
print(z_1 + z_2)
print(z_1 * z_2)
