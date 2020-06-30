num_init = int(input("Здравствуйте!Введите целое положительное число"))
max_ = 0
num = num_init
while num > 0:
    digit = num % 10
    if digit > max_:
        max_ = digit
        if max_ == 9:
            break
    num = num // 10
print(f'максимальная цифра в числе - это {max_}')
