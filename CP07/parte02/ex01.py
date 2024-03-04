from random import randint

matriz = []
contador = 0

for i in range(4):
    matriz += [list(randint(1, 20) for i in range(4))]


for linha in matriz:
    for elemento_coluna in linha:
        if elemento_coluna > 10:
            contador += 1

print(matriz)
print(f"{contador} números são maiores que 10")