from random import randint

matriz = []

for i in range(5):
    matriz += [list(randint(1, 50) for i in range(5))]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()

encontrar = int(input("Digite um valor para encontrar na matriz: "))
posicao = []

for linha in matriz:
    for coluna_elemento in linha:
        if encontrar == coluna_elemento:
            posicao = [matriz.index(linha) + 1, linha.index(coluna_elemento) + 1]


if posicao == []:
    print(f"Não encontrado!")

else:
    print(f"Linha: {posicao[0]}. Coluna: {posicao[1]}")