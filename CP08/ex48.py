from random import randint

def soma_elementos(vetor):
    soma = 0

    for linha in range(len(vetor)):
        for coluna in range(len(vetor)):
            if linha == 0 and coluna != 0 or linha == 1 and coluna == 2:
                soma += vetor[linha][coluna]

    return soma

matriz = []

for i in range(3):
    matriz += [list(randint(1, 100) for i in range(3))]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=' ')

    print()

print(soma_elementos(matriz))