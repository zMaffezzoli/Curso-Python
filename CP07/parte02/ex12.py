from random import randint

matriz = []
matriz_transposta = []
soma = 0

for i in range(3):
    matriz += [list(randint(1, 50) for i in range(3))]
    matriz_transposta += [list(0 for i in range(3))]

for linha in range(3):
    for elemento_coluna in range(3):
        matriz_transposta[elemento_coluna][linha] = matriz[linha][elemento_coluna]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")

    print()

print()

for linha in matriz_transposta:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")

    print()