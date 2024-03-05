def linha(matriz, n):
    return [i for i in matriz[n]]

def coluna(matriz, n):
    return [i[n] for i in matriz]

def produto_matricial(matrizA, matrizB):
    matrizAlinha = len(matrizA)
    matrizAcoluna = len(matrizA[0])
    matrizBlinha = len(matrizB)
    matrizBcoluna = len(matrizB[0])
    resultado = []

    for i in range(matrizAlinha):
        resultado.append([])

        for j in range(matrizBcoluna):
            listMult = [x*y for x, y in zip(linha(matrizA, i), coluna(matrizB, j))] # Mescla as linhas com as colunas
            resultado[i].append(sum(listMult))

    return resultado


matrizA = [[3, 2], [5, -1]]

matrizB = [[6, 4, -2], [0, 7, 1]]

print(produto_matricial(matrizA, matrizB))