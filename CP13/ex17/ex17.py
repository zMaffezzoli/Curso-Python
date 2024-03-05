from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "matriz.txt")
arquivotxt2 = path.join(caminho, "matriz_saida.txt")

try:

    arquivo2 = open(arquivotxt2, mode="w+", encoding="UTF-8")

    with open(arquivotxt, mode="r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
        linha_matriz = linhas[0][linhas[0].index("/") + 1]
        coluna_matriz = linhas[0][linhas[0].index("/") + 3]
        
        posicoes = [linhas[-1][linhas[-1].index("/"):]]
        posicoes = posicoes[0].replace("/", "")
        posicoes = posicoes.replace("x", ",")
        posicoes = posicoes.split(" ")
        
        for linhas in range(int(linha_matriz)):
            for elemento_coluna in range(int(coluna_matriz)):
                varLC = str(linhas + 1) + ',' + str(elemento_coluna + 1)
                
                if varLC in posicoes:
                    arquivo2.write("0 ")
                else: 
                    arquivo2.write("1 ")
                        
            arquivo2.write("\n")
                    
    arquivo2.close()

except Exception as err:
    print(f"Não foi possível criar um arquivo e escrever-lo, erro: {err}")