from sys import argv

try:
    script, hours, stavka, premia = argv
    print("Этот скрипт называется: ", script)
    print("Выработка в часах: ", hours)
    print("Ставка в час: ", stavka)
    print("Премия: ", premia)


    def my_func(hours, stavka, premia):
        """Считает заработную плату по введенным параметрам"""
        return f'Ваша заработная плата равна: {int(hours) * int(stavka) + int(premia)}'
    print(my_func(hours, stavka, premia))

except ValueError:
    print('Вам необходимо передать еще дополнительно три аргумента.Воспользуйтесь командной строкой,'
          'терминалом или PyCharm')
