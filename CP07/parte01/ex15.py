from random import randint

lista = list(randint(1, 20) for i in range(20))
print(lista)

print(list(set(lista)))