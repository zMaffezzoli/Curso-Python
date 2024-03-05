from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "pessoas.txt")
arquivotxt2 = path.join(caminho, "idades.txt")

data_atual = (13, 2, 2024)
try:
    arquivo2 = open(arquivotxt2, mode="w", encoding="UTF-8")

    with open(arquivotxt, mode="r", encoding="UTF-8") as arquivo:
        
        pessoas = arquivo.readlines()
        pessoas = [i.split(" ") for i in pessoas]
        
        for pessoa in pessoas:
            ano = data_atual[2] - int(pessoa[3][:-1])

            if (data_atual[0] <= int(pessoa[1]) and (data_atual[1] <= int(pessoa[2]))):
                ano -= 1

            
            arquivo2.write(str(pessoa[0]) + " " + str(ano) + " anos\n")

    arquivo2.close()


except Exception as err:
    print(f"Não foi possível abrir o arquivo e adicionar em outro arquivo, erro: {err}")