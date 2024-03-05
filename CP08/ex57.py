from random import randint

def soma_coluna(matriz, coluna):
    soma_coluna = 0

    for linha in matriz:
        soma_coluna += linha[coluna-1]

    return f"Soma dos elementos da {coluna} coluna: {soma_coluna}"

matriz = []

for i in range(7):
    matriz += [list(randint(1, 100) for i in range(6))]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')

    print()

print(soma_coluna(matriz, 1))
print(soma_coluna(matriz, 2))