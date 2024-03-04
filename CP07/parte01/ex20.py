from random import randint

lista = list(randint(0, 50) for i in range(10))

impares = []

for i in lista:
    if i % 2:
        impares += [i]

print(lista)
print(impares)

for indice, valor in enumerate(lista):
    if not (indice % 2):
        print(valor, end= " ")

    else:
        print(valor)

print()

for indice, valor in enumerate(impares):
    if not (indice % 2):
        print(valor, end= " ")

    else:
        print(valor)