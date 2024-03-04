aluno1 = ["A", "B", "B", "C", "D", "A", "D", "C", "A", "B"] 
aluno2 = ["B", "C", "A", "C", "B", "D", "B", "C", "D", "C"]
aluno3 = ["A", "C", "B", "A", "D", "A", "D", "C", "B", "C"] 
aluno4 = ["C", "D", "C", "B", "C", "B", "A", "B", "A", "D"]
aluno5 = ["A", "B", "B", "D", "A", "C", "D", "D", "B", "A"] 

gabarito = ["A", "C", "B", "A", "D", "A", "D", "C", "B", "C"]
respostas = [aluno1] + [aluno2] + [aluno3] + [aluno4] + [aluno5]

resultado = [[] for i in range(5)]

for i in range(10):

    if gabarito[i] == respostas[0][i]:
        resultado[0] += [1]

    if gabarito[i] == respostas[1][i]:
        resultado[1] += [1]
    
    if gabarito[i] == respostas[2][i]:
        resultado[2] += [1]

    if gabarito[i] == respostas[3][i]:
        resultado[3] += [1]

    if gabarito[i] == respostas[4][i]:
        resultado[4] += [1]


for i in range(1, 6):
    print(f"Aluno {i} tirou: {sum(resultado[i-1])}")