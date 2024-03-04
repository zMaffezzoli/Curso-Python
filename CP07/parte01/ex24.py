aluno1 = [1, 1.85]
aluno2 = [2, 1.90]
aluno3 = [3, 1.60]
aluno4 = [4, 1.47]
aluno5 = [5, 1.67]
aluno6 = [6, 1.86]
aluno7 = [7, 1.36]
aluno8 = [8, 1.58]
aluno9 = [9, 1.89]
aluno10 = [10, 1.45]

todas_alturas = [aluno1[1], aluno2[1], aluno3[1], aluno4[1], aluno5[1], aluno6[1], aluno7[1], aluno8[1], aluno9[1], aluno10[1]]
todos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]

maior_altura = max(todas_alturas)
menor_altura = min(todas_alturas)

for i in range(len(todos)):

    if todas_alturas[i] == maior_altura:
        print(f"Número pessoa: {todos[i][0]}, sua altura: {todos[i][1]}")

    if todas_alturas[i] == menor_altura:
        print(f"Número pessoa: {todos[i][0]}, sua altura: {todos[i][1]}")