from random import randint

# Nº Matriculas
aluno1 = [1]
aluno2 = [2]
aluno3 = [3]
aluno4 = [4]
aluno5 = [5]

matriz = [aluno1] + [aluno2] + [aluno3] + [aluno4] + [aluno5]

matricula_maior_nota = 0
maior_nota = 0

media = 0

for i in range(2):
    aluno1 += [(randint(1, 10))]
    aluno2 += [(randint(1, 10))]
    aluno3 += [(randint(1, 10))]
    aluno4 += [(randint(1, 10))]
    aluno5 += [(randint(1, 10))]

for aluno in matriz:
    print(F"Matrícula: {aluno[0]}. Média das provas: {aluno[1]}. Média dos trabalhos: {aluno[2]}")
    aluno.append((aluno[1] + aluno[2]) / 2)

for aluno in range(len(matriz)):
    media += matriz[aluno][3]

    if aluno == 0:
        maior_nota = matriz[aluno][3]
        matricula_maior_nota = matriz[aluno][0]

    if aluno != 0 and matriz[aluno][3] >= maior_nota:
        maior_nota = matriz[aluno][3]
        matricula_maior_nota = matriz[aluno][0]

print(f"A matricula do aluno que teve a maior nota final é: {matricula_maior_nota}")
print(f"A média aritmética das notas finais é: {media / len(matriz)}")