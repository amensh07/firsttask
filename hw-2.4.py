my_str = input('Введите любую фразу')
my_str = my_str.split()
print(my_str)
for ind, i in enumerate(my_str, 1):
    if len(i) > 10:
        print(ind, i[: 10])
    else:
        print(ind, i)
