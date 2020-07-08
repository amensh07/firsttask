def sum_num():
    res = 0
    while True:
        list_number = input("Введите числа, для выхода нажмите 'Q' ").split()
        for _ in list_number:
            if _ == "Q":
                return res
            else:
                try:
                    res += int(_)
                except ValueError:
                    print("To exit the program, enter - 'Q'.")
        print(f"Сумма чисел - {res}")


print(sum_num())
