def my_del(m, n):
    """Функция, которая делит """
    try:
        m, n = int(m), int(n)
        d = m / n
        return d

    except ZeroDivisionError:
        print('Делить на ноль нельзя!')


print(my_del(input('Введите первое число ')), input('Введите второе число '))
