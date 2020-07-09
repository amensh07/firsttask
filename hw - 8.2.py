class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = input('Введите числитель ')
num2 = input('Введите знаменатель ')
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise MyOwnErr("Знаменатель не должен быть равным нулю!")

except ValueError:
    print('Ошибка!')

except MyOwnErr as err:
    print(err)
else:
    res = num1 / num2
    print(res)
