my_list = [10, 8, 6, 2, 1]
new = int(input('Введие новый элемент рейтинга'))
for i in my_list:
    if i > new >= my_list[my_list.index(i) + 1]:
        my_list.insert(my_list.index(i) + 1, new)
        print(my_list)
        break
    elif new > i:
        my_list.insert(0, new)
        print(my_list)
        break
    elif new <= my_list[-1]:
        my_list.append(new)
        print(my_list)
        break
