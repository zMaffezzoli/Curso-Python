from random import randint

aluno1 = list(randint(1, 10) for i in range(3))
aluno2 = list(randint(1, 10) for i in range(3))
aluno3 = list(randint(1, 10) for i in range(3))
aluno4 = list(randint(1, 10) for i in range(3))
aluno5 = list(randint(1, 10) for i in range(3))
aluno6 = list(randint(1, 10) for i in range(3))
aluno7 = list(randint(1, 10) for i in range(3))
aluno8 = list(randint(1, 10) for i in range(3))
aluno9 = list(randint(1, 10) for i in range(3))
aluno10 = list(randint(1, 10) for i in range(3))

piores_prova1 = 0
piores_prova2 = 0
piores_prova3 = 0

matriz = [aluno1] + [aluno2] + [aluno3] + [aluno4] + [aluno5] + [aluno6] + [aluno7] + [aluno8] + [aluno9] + [aluno10]

for i in matriz:

    if i.index(min(i)) == 0:
        piores_prova1 += 1

    elif i.index(min(i)) == 1:
        piores_prova2 += 1

    else:
        piores_prova3 += 1

print(matriz)
print(f"Quantidade de alunos que a pior nota foi na prova 1: {piores_prova1}")
print(f"Quantidade de alunos que a pior nota foi na prova 2: {piores_prova2}")
print(f"Quantidade de alunos que a pior nota foi na prova 3: {piores_prova3}")