from random import randint

matriz = []

for i in range(4):
    matriz += [list(randint(1, 50) for i in range(4))]

maior = 0
posicao = []

for linha in matriz:
    for elemento_coluna in linha:
        if elemento_coluna >= maior:
            maior = elemento_coluna
            posicao = [matriz.index(linha) + 1, linha.index(maior) + 1]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()

print(f"Maior valor: {maior}. Posição: Linha: {posicao[0]}, Coluna: {posicao[1]}")