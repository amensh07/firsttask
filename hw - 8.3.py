class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    if input("Для выхода из программы 'Q', "
             "для продолжения ввода элементов в список нажмите 'Enter'"):
        break
    try:
        new = input('Введие новый элемент списка')
        my_list.append(new)
        new_list = []
        for i in my_list:
            try:
                type(int(i)) == int
                new_list.append(i)
                print(new_list)
            except ValueError:
                raise MyOwnErr("Нужно ввести число")
    except MyOwnErr as err:
        print(err)
