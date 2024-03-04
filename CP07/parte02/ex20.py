from random import randint

matriz = []

for i in range(3):
    matriz += [list(randint(0, 20)for j in range(6))]

coluna_impar = 0
media = 0
soma_coluna1e2 = 0

for linha in range(len(matriz)):
    for elemento_coluna in range(6):

        if not (elemento_coluna % 2):
            coluna_impar += matriz[linha][elemento_coluna]

        if elemento_coluna == 1 or elemento_coluna == 3:
            media += matriz[linha][elemento_coluna]
            
        if elemento_coluna == 0 or elemento_coluna == 1:
            soma_coluna1e2 += matriz[linha][elemento_coluna]

for linha in matriz:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()

print(f"Soma de todos os elementos das colunas ímpares: {coluna_impar}")
print(f"Média aritmética dos elementos da segunda e da quarta coluna: {media/6}")

for linha in range(len(matriz)):

    for elemento_coluna in range(6):

        if elemento_coluna == 5:
            matriz[linha][elemento_coluna] = soma_coluna1e2

for linha in matriz:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()