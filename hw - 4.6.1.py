""" Итератор генерирует целые числа. Диапазон значений указывает пользователь """
from itertools import count

end_num = int(input('Укажите конечное число '))
for el in count(int(input('Укажите стартовое число '))):
    if el > end_num:
        break
    else:
        print(el)


