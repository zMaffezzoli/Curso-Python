from random import randint

matriz1 = []
matriz2 = []
matriz3 = []

maior1 = 0
maior2 = 0
posicao1 = []
posicao2 = []

for i in range(4):
    matriz1 += [list(randint(1, 50) for i in range(4))]
    matriz2 += [list(randint(1, 50) for i in range(4))]
    matriz3 += [list(0 for i in range(4))]

for linha in matriz1:
    for elemento_coluna in linha:
        if elemento_coluna >= maior1:
            maior1 = elemento_coluna
            posicao1 = [matriz1.index(linha), linha.index(elemento_coluna)]

for linha in matriz2:
    for elemento_coluna in linha:
        if elemento_coluna >= maior2:
            maior2 = elemento_coluna
            posicao2 = [matriz2.index(linha), linha.index(elemento_coluna)]


matriz3[posicao1[0]][posicao1[1]] = maior1
matriz3[posicao2[0]][posicao2[1]] = maior2


for linha in matriz1:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()

print()

for linha in matriz2:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()

print()

for linha in matriz3:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()