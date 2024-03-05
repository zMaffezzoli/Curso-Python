from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "alunos.txt")

try:
    nomes = []
    notas = []

    numero_alunos = int(input("Digite o número de alunos na disciplina: "))

    for i in range(numero_alunos):
        nome = input("Digite o nome do aluno: ")
        nomes.append(nome)

        nota = []
        for i in range(3):
            nota_individual = float(input(f"Digite 3 notas para {nome}: "))
            nota.append(nota_individual)
        
        notas.append(nota)

    with open(arquivotxt, mode="w", encoding="UTF-8") as arquivo:

        for i in range(len(nomes)):
            if len(nomes[i]) < 40:
                nome_branco = nomes[i] + " " * (40 - len(nomes[i]))
            arquivo.write(f"{nome_branco} Media: {sum(notas[i]) / 3} \n")


except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")
