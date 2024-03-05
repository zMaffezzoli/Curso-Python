from random import randint

def soma_matriz(matriz):
    soma = 0

    for linha in matriz:
        for elemento in linha:
            soma += elemento

    return soma

matriz = []

for i in range(4):
    matriz += [list(randint(1, 100) for i in range(4))]


for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')

    print()

print(soma_matriz(matriz))