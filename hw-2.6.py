features = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
my_list = []
analysis = {'название': [], 'цена': [], 'количество': [], 'ед': []}
n = 0
while True:
    if input("Для выхода из программы нажмите 'Q', для продолжения 'Enter'"):
        break
    n = + 1
    for f in features.keys():
        _ = input(f'Введите значение свойства "{f}": ')
        features[f] = int() if (f == 'цена' or f == 'количество') else _
        analysis[f].append(features[f])
    my_list.append((n, features))
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analysis.items():
        print(f'{key[:25]:>30}:{value}')
    print("*" * 30)
