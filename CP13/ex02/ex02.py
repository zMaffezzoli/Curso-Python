from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

try:
    with open(arquivotxt, mode="r", encoding='UTF-8') as arquivo:
    
        print(f"O arquivo possui {len(arquivo.readlines())} linhas")

except Exception as err:
    print(f"Não foi possível ler a quantidade de linhas {err}")