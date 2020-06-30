""" Итератор повторяет элементы списка. Список определен заранее """


from itertools import cycle

с = 0
end_num = int(input('Сколько раз повторять элементы списка - '))
for el in cycle(input('Введите что-либо ')):
    if с > end_num:
        break
    print(el)
    с += 1
