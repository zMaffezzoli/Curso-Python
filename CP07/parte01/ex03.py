from random import randint

lista = list(randint(1, 20) for i in range(10))
quadrados = []

for i in lista:
    quadrados.append(i**2)

print(lista)
print(quadrados)