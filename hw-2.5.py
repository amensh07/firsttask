my_list = [10, 8, 6, 3, 3, 3, 2, 1]
new = int(input('Введие новый элемент рейтинга'))
for i in my_list:
    if new > i:
        my_list.insert(0, float(new))
        print(my_list)
        break
    elif new >= my_list[my_list.index(i) + 1]:
        my_list.insert(my_list.index(i) + my_list.count(new) + 1, float(new))
        print(my_list)
        break
    elif new <= my_list[-1]:
        my_list.append(new)
        print(my_list)
        break
