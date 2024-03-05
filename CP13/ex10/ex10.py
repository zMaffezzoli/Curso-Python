from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "cidades.txt")
arquivotxt2 = path.join(caminho, "maior_cidade.txt")

populacao_maior = -1
cidade = ""

try:
    with open(arquivotxt, mode="r", encoding="utf-8") as arquivo:
        for i in arquivo.readlines():
            if int(i[40:-1]) > populacao_maior:
                populacao_maior = int(i[40:-1])
                cidade = i[:40].replace(" ", "")


    with open(arquivotxt2, mode="w", encoding="utf-8") as arquivo2:
        arquivo2.write(str(cidade) + " " + str(populacao_maior))

except Exception as err:
    print(f"Não foi possível ler o arquivo e criar outro, erro: {err}")