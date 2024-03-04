matriz = []

for i in range(10):
    matriz += [list(0 for i in range(10))]

for i in range(len(matriz)):
    for j in range(len(matriz)):

        if i == j:
            matriz[i][j] = (3 * (i**2)) - 1

        elif i < j:
            matriz[i][j] = (2 * i) + (7 * j) - 2

        else:
            matriz[i][j] = ((4 * (i**3)) - (5 * (j**2))) + 1

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()