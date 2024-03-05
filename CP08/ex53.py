def matriz_identidade(matriz):

    matriz_identidade = [[] for i in range(len(matriz))]

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if linha == coluna:
                matriz_identidade[linha].append(1)

            else:
                matriz_identidade[linha].append(0)
    

    print(matriz_identidade)
    if matriz == matriz_identidade:
        return f"É matriz identidade"
    
    return f"Não é matriz identidade"


matriz1 = [[1, 0, 0], [0 ,1, 0], [0, 0, 1]]
matriz2 = [[1, 2,3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [4, 3, 2, 1]]
matriz3 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

print(matriz_identidade(matriz1))
print(matriz_identidade(matriz2))
print(matriz_identidade(matriz3))