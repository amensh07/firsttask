def people(name, surname, born, city, email, phone):
    return ' '.join([name, surname, born, city, email, phone])


print(people(name=input('Ваше имя '), surname=input('Ваша фамилия '), born=input('Ваш год рождения '),
             city=input('Ваш город '), email=input('Ваш электронный адрес '), phone=input('Ваш номер телефона ')))
