from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

try:

    with open(arquivotxt, mode='r', encoding='UTF-8') as arquivo:
        numero_caracteres = len(arquivo.read().replace("\n", ""))
        arquivo.seek(0)

        numero_linhas = len(arquivo.readlines())
        arquivo.seek(0)

        linhas = arquivo.readlines()
        numero_palavras = []
        
        for i in linhas:
            numero_palavras.extend(i.split(" "))
         
        while "" in numero_palavras:
            numero_palavras.pop(numero_palavras.index(""))

        print(f"Número de caracteres: {numero_caracteres} / Número de linhas: {numero_linhas} / Número palavras: {len(numero_palavras)}")
        
except Exception as err:
    print(f"Não foi possível ler o arquivo e criar outro, erro: {err}")