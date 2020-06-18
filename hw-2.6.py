key = ["название", "цена", "количество", "ед"]
my_list = []
analysis = []
quest = int(input('Сколько будет товаров?'))
n = 1
while n <= quest:
    name = input('Напишите название товара')
    price = input('Уточните цену товара')
    qty = input('Подскажите количество товара')
    unit = input('Напишите единицы измерения')
    values = [name, price, qty, unit]
    print(values)
    my_dict = dict(zip(key, values))
    print(my_dict)
    my_list.append((n, dict))
    n += 1
    analysis = dict({'название': my_dict.get('название'), 'цена': my_dict.get('цена'),
                     'количество': my_dict.get('количество'),
                     'ед': my_dict.get('ед')})

    print(analysis)
