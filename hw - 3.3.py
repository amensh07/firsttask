def my_func(a, b, c):
    if a >= b and b >= c:
        return a + b
    elif c > a and b > a:
        return c + b
    else:
        return c + a


print(my_func(int(input('Введите первое число ')), int(input('Введите второе число ')),
              int(input('Введите третье число '))))
