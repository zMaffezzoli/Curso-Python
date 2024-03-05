from random import randint

def matriz_transposta(vetor):
    matriz_transposta = [[] for i in range(len(vetor))]

    for linha in range(len(vetor)):
        for coluna in range(len(vetor)):
                matriz_transposta[linha].append(vetor[coluna][linha])

    return matriz_transposta

matriz = []

for i in range(3):
    matriz += [list(randint(1, 100) for i in range(3))]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=' ')

    print()

print()
for linha in matriz_transposta(matriz):
    for elemento_coluna in linha:
        print(elemento_coluna, end=' ')

    print()