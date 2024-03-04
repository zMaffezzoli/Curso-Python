from random import randint

lista = list(randint(1, 100) for i in range(6))

pares = []
impares = []

for i in lista:

    if not(i % 2):
        pares.append(i)

    else:
        impares.append(i)

print(f"Números pares: {pares}")
print(f"A soma dos números pares: {sum(pares)}")
print(f"Números impares: {impares}")
print(f"Quantidade de números impares: {len(impares)}")