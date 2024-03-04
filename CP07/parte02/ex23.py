from random import randint

matrizA = []
matrizB = []

for i in range(3):
    matrizA += [list(randint(0, 20)for j in range(3))]

for linha in range(3):

    for elemento_coluna in range(3):

        matrizB.append(matrizA[linha][elemento_coluna] ** 2)

coluna1 = matrizB[0:3]
coluna2 = matrizB[3:6]
coluna3 = matrizB[6:]

matrizB = [coluna1] + [coluna2] + [coluna3]

for linha in matrizA:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()

print()

for linha in matrizB:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()