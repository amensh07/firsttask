my_file = open("my_file_5(1-2).txt", 'a', encoding="utf-8")
length = input('Введити свою фразу ')
if length == 0:
    my_file.close()
else:
    my_file.writelines(length + '\n')
my_file.close()


