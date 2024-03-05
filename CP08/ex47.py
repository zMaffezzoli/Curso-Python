from random import randint

def conta_maior10(vetor):
    maiores = 0

    for linha in vetor:
        for elemento_coluna in linha:
            if elemento_coluna > 10:
                maiores += 1

    return maiores

matriz = []

for i in range(4):
    matriz += [list(randint(1, 20) for i in range(4))]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=' ')

    print()

print(conta_maior10(matriz))