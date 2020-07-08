def my_func(x, y):
    return x ** y


print(my_func(2, -3))


def my_func2(x, y):
    x = float(x)
    y = int(y)
    if x <= 0 or y >= 0:
        return 'X должно быть больше 0, а Y меньше 0'
    else:
        result = 1
        for _ in range(abs(y)):
                result *= 1 / x
        return f'Результат возведения х в степень у: {round(result, 6)}'


print(my_func2(input('Введите действительное целое число х = '), input('Введите целое отрицательное число у = ')))
