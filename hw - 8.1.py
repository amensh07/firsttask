import re


class Data:
    def __init__(self, my_data):
        self.my_data = str(my_data)

    @classmethod
    def class_met(cls, my_data):
        new_list = re.findall("\d+", my_data)
        print(new_list)
        return int(new_list[0]), int(new_list[1]), int(new_list[2])

    @staticmethod
    def static_met(my_data):
        new_list = re.findall("\d+", my_data)
        print(new_list)
        if 1 > int(new_list[0]) or int(new_list[0]) > 31:
            print('Неверная дата')
        else:
            print(int(new_list[0]))
        if 0 > int(new_list[1]) or int(new_list[0]) > 12:
            print('Неверная дата')
        else:
            print(int(new_list[1]))
        if 0 > int(new_list[2]) or int(new_list[0]) > 2020:
            print('Неверная дата')
        else:
            return int(new_list[2])


new_data = Data('22 - 14 - 2001')
print(Data.class_met('22 - 14 - 2001'))
print(Data.static_met('22 - 14 - 2001'))
