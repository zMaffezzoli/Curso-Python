from random import randint

lista1 = list(randint(1, 20) for i in range(10))
lista2 = list(randint(1, 20) for i in range(10))
lista3 = []

for i in range(len(lista1)):

    if not (i % 2):
        lista3 += [lista1[i]]

    else:
        lista3 += [lista2[i]]


print(lista1)
print(lista2)
print(lista3)