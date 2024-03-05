from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "aluno.txt")
arquivotxt2 = path.join(caminho, "aluno_ordenado.txt")

try:
    arquivo2 = open(arquivotxt2, mode="w")

    with open(arquivotxt, mode='r', encoding='utf-8') as arquivo:
        linha = arquivo.read()
        
        nome = linha[0:40]
        nome = nome.replace(" ", "")
        
        notas = linha[40:].split(" ")
        notas = [float(i) for i in notas]
        notas.sort()

        arquivo2.write(f"{nome} ")
        
        for i in notas:
            arquivo2.write(f"{i} ")
        
    arquivo2.close()

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")
