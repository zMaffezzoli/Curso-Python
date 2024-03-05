from random import randint

def uniao_vetor(matrizA, matrizB):
    matrizA = set(matrizA[0:2])
    matrizB = set(matrizB[0:2])
    
    return matrizA.union(matrizB)

matrizA = [randint(1,20) for i in range(10)]
matrizB = [randint(1,20) for i in range(10)]

print(matrizA)
print(matrizB)
print(f"União dos dois primeiros elementos das matrizes {uniao_vetor(matrizA, matrizB)}")