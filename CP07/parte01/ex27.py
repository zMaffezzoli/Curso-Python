from random import randint

lista = list(randint(1, 100) for i in range(1, 11))

primos = []

for numero in lista:

    if numero > 1:
        for j in range(2, numero):
            if not numero % j:
                break

        else:
            primos.append(numero)

print(lista)
print(primos)

for i in primos:
    print(f"Posição do primo {i} é {lista.index(i) + 1}")