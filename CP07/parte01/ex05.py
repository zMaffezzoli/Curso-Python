from random import randint

lista = list(randint(1, 20) for i in range(10))

pares = []

for i in lista:
    if not i % 2:
        pares.append(i)

    else:
        pass

print(lista)
print(f"Quantos pares temos: {len(pares)}. A soma deles é {sum(pares)}")