from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "pessoas.txt")
arquivotxt2 = path.join(caminho, "idades.txt")

ano_atual = 2024

try:
    arquivo2 = open(arquivotxt2, mode="w", encoding="UTF-8")

    with open(arquivotxt, mode="r", encoding="UTF-8") as arquivo1:
        pessoas = arquivo1.readlines()

        for pessoa in pessoas:
            nome = pessoa[:40].replace(" ","")
            ano = ano_atual - int(pessoa[41:-1])

            if ano > 18:
                arquivo2.write(f"{nome} é maior de idade\n")

            elif ano < 18:
                arquivo2.write(f"{nome} é menor de idade\n")

            else:
                arquivo2.write(f"{nome} está entrando na maior idade\n")
            
    arquivo2.close()

except Exception as err:
    print(f"Não foi possível abrir o arquivo e criar outro, erro: {err}")