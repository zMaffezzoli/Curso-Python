from random import randint

def soma_diagonal(matriz):
    diagonal_principal = 0
    diagonal_secundaria = 0

    for linha in range(3):
        for coluna in range(3):
            if linha == 0 and coluna == 2 or linha == 1 and coluna == 1 or linha == 2 and coluna == 0:
                diagonal_secundaria += matriz[linha][coluna]

            if linha == 0 and coluna == 0 or linha == 1 and coluna == 1 or linha == 2 and coluna == 2:
                diagonal_principal+= matriz[linha][coluna]

    return f"Diagonal principal: {diagonal_principal}. Diagonal secundária: {diagonal_secundaria}"


matriz = []

for i in range(3):
    matriz += [list(randint(1, 100) for i in range(3))]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')

    print()

print(soma_diagonal(matriz))