my_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(my_dict)
your_season = input('Введите месяц в виде целого числа от 1 до 12_')
print(my_dict.get(int(your_season)))

my_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
           'autumn', 'autumn', 'winter']
your_season = input('Введите месяц в виде целого числа от 1 до 12_')
print(my_list[int(your_season) - 1])
