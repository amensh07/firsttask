print('Я хочу узнать твои финансовые результаты. Введите значение выручки')
rev = float(input())
print('Также введите значение издержек')
cost = float(input())
if rev > cost:
    print('Вы работаете в плюс. Поздравляем!')
    rent = float(((rev - cost) / rev))
    print(f'Ваша рентабельность составила {rent:.2f}')
    print('Я могу посчитать прибыль на одного сотрудника.Для этого введите количество ваших сотрудников')
    emp = int(input())
    result = (rev - cost) / emp
    print(f'Прибыль на одного сотрудника составила {result:.2f}')
elif cost == rev:
    print('Вы работаете в ноль')
else:
    print('Вы работаете в убыток, пересмотрите свои расходы')
