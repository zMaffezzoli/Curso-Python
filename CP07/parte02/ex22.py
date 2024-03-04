from random import randint

matrizA = []
matrizB = []
matrizC = []

for i in range(3):
    matrizA += [list(randint(0, 20)for j in range(3))]
    matrizB += [list(randint(0, 20)for j in range(3))]

for linha in range(3):

    for elemento_coluna in range(3):

        matrizC.append(matrizA[linha][elemento_coluna] * matrizB[linha][elemento_coluna])

coluna1 = matrizC[0:3]
coluna2 = matrizC[3:6]
coluna3 = matrizC[6:]

matrizC = [coluna1] + [coluna2] + [coluna3]

for linha in matrizA:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()

print()

for linha in matrizB:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()

print()

for linha in matrizC:
    for coluna_elemento in linha:
        print(coluna_elemento, end=" ")

    print()