from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "alunos.txt")

try:
    nomes = []
    notas = []

    numero_alunos = int(input("Digite o número de alunos na disciplina: "))

    for i in range(numero_alunos):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))

        nomes.append(nome)
        notas.append(nota)

    with open(arquivotxt, mode="w", encoding="UTF-32") as arquivo:

        for i in range(len(nomes)):
            arquivo.write(f"{nomes[i]} - {notas[i]}\n")

    with open(arquivotxt, mode="r", encoding="UTF-32") as arquivo:
        linhas = arquivo.readlines()
        nomes = []
        notas = []
        
        for i in linhas:
            nomes.append(i[:(i.index("-") - 1)])        
            notas.append(float(i[(i.index("-") + 2):-1]))

        
        print(f"{nomes[notas.index(max(notas))]} teve a maior nota. Nota: {notas[notas.index(max(notas))]}")
        
except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")