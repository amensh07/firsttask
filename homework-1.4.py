print('Здравствуйте!Введите целое положительное число')
num = int(input())
max = num % 10
while num >=1:
    num = num//10
    if num % 10 > max:
        max = num%10
    if num > 9:
        continue
    else:
        print(f'максимальная цифра в числе - это {num}')
    break
