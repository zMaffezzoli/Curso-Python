from random import randint
import copy

matriz = []

for i in range(4):
    matriz += [list(randint(1, 20) for i in range(4))]

matriz_triangular = copy.deepcopy(matriz)

for linha in range(4):
    for elemento_coluna in range(4):
        if linha == 0 and elemento_coluna > 0:
            matriz_triangular[linha][elemento_coluna] = 0

        elif linha == 1 and elemento_coluna > 1:
            matriz_triangular[linha][elemento_coluna] = 0

        elif linha == 2 and elemento_coluna > 2:
             matriz_triangular[linha][elemento_coluna] = 0

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")

    print()

print()

for linha in matriz_triangular:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")

    print()