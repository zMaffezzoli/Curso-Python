from random import randint

matriz = []

coluna1 = 0
coluna2 = 0
coluna3 = 0

for i in range(3):
    matriz += [list(randint(1, 20) for i in range(3))]

for linha in range(len(matriz)):

    for elemento_coluna in range(len(matriz)):
        
        if elemento_coluna == 0:
            coluna1 += matriz[linha][elemento_coluna]

        elif elemento_coluna == 1:
            coluna2 += matriz[linha][elemento_coluna]

        else:
            coluna3 += matriz[linha][elemento_coluna]

matriz2 = [coluna1, coluna2, coluna3]

for linha in matriz:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()

print(matriz2)