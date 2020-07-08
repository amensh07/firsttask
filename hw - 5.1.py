my_file = open("my_file_5(1-2).txt", 'a', encoding="utf-8")
while True:
    length = input('Введити свою фразу ')
    if not length:
        break
    my_file.writelines(length + '\n')
my_file.close()


