my_list = input('напишите что-нибудь_')
print(list(my_list))
if len(my_list) % 2 == 0:
    for i in my_list:
        # print(my_list.index(el))
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
else:
    print('')
