from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "entrada.txt")
arquivotxt2 = path.join(caminho, "saida.txt")

try:
    with open(arquivotxt, mode="r", encoding="UTF-8") as arquivo:
        linhas = arquivo.read()

        with open(arquivotxt2, mode="w", encoding="UTF-8") as arquivo2:
            arquivo2.write(linhas[::-1])

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")
