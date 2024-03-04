from random import randint

lista = list(randint(-10, 10) for i in range(10))

print(lista)

for indice, valor in enumerate(lista):
    if valor < 0:
        lista[indice] = 0

    else:
        pass

print(lista)