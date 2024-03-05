from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "alunos.txt")

try:
    with open(arquivotxt, mode="w+", encoding="UTF-8") as arquivo:
        while True:
                print(f"\na) Inserir aluno e notas \nb) Exibir alunos e médias \nc) Exibir alunos aprovados \nd) Exibir alunos reprovados \ne) sair")

                opcao = input("Digite a opção desejada: ")

                if opcao == "a":
                    nome = input("Digite o nome do aluno: ")
                    
                    arquivo.write(f"{nome} - ")

                    for i in range(3):
                        nota = float(input("Digite uma nota: "))
                        arquivo.write(f"{nota} ")

                    arquivo.write("\n")

                elif opcao == "b":
                    arquivo.seek(0)
                    linhas = arquivo.readlines()
                    notas = []
                    medias_alunos = []

                    for i in linhas:
                        notas.append(i[(i.index("-") + 2):-2].split(" "))

                    for i in notas:
                        media = 0
                        for nota in i:
                            media += float(nota)
                        medias_alunos.append(media)

                    for i in range(len(linhas)):
                        print(f"{linhas[i][0:(linhas[i].index('-') -1)]}: Média: {medias_alunos[i] / 3}")

                elif opcao == "c":
                    arquivo.seek(0)
                    linhas = arquivo.readlines()
                    notas = []
                    medias_alunos = []

                    for i in linhas:
                        notas.append(i[(i.index("-") + 2):-2].split(" "))

                    for i in notas:
                        media = 0
                        for nota in i:
                            media += float(nota)
                        medias_alunos.append(media)

                    for i in range(len(linhas)):
                        if (medias_alunos[i] / 3) >= 7.0:
                            print(f"{linhas[i][0:(linhas[i].index('-') -1)]} Aprovado")

                elif opcao == "d":
                    arquivo.seek(0)
                    linhas = arquivo.readlines()
                    notas = []
                    medias_alunos = []

                    for i in linhas:
                        notas.append(i[(i.index("-") + 2):-2].split(" "))

                    for i in notas:
                        media = 0
                        for nota in i:
                            media += float(nota)
                        medias_alunos.append(media)

                    for i in range(len(linhas)):
                        if (medias_alunos[i] / 3) <= 7.0:
                            print(f"{linhas[i][0:(linhas[i].index('-') -1)]} Reprovado")

                else:
                    break

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")