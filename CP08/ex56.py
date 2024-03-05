from random import randint 

def soma_linha(matriz, linha):
    return f"Soma dos elementos da {linha} linha: {sum(matriz[linha-1])}"

matriz = []

for i in range(7):
    matriz += [list(randint(1, 100) for i in range(6))]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')

    print()

print(soma_linha(matriz, 1))
print(soma_linha(matriz, 5))