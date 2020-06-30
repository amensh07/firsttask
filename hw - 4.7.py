from math import factorial

my_list = [1, 6, 8, 12]


def generator():
    for el in my_list:
        yield factorial(el)


g = generator()
print(g)

for el in g:
    print(el)
