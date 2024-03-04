from random import randint

matriz = []
soma = 0

for i in range(3):
    matriz += [list(randint(1, 50) for i in range(3))]

for linha in range(3):
    for elemento_coluna in range(3):
        if linha == 0 and elemento_coluna == 1 or linha == 0 and elemento_coluna == 2:
            soma += matriz[linha][elemento_coluna]

        elif linha == 1 and elemento_coluna == 2:
            soma += matriz[linha][elemento_coluna]


for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")

    print()

print(f"A soma dos valores acima da diagonal principla é: {soma}")