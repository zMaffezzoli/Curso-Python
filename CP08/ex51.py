from random import randint

def soma_diagonal(vetor):
    soma = 0

    for linha in range(len(vetor)):
        for coluna in range(len(vetor)):
            if linha == 0 and coluna == 2 or linha == 1 and coluna == 1 or  linha == 2 and coluna == 0:
                soma += vetor[linha][coluna]

    return soma

matriz = []

for i in range(3):
    matriz += [list(randint(1, 100) for i in range(3))]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=' ')

    print()

print(soma_diagonal(matriz))