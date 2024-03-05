from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

with open(arquivotxt) as arquivo: # Cria um contexto, onde fora do block o contexto é fechado

    print(arquivo.readlines())
    print()

    arquivo.seek(30) # Movimenta o cursor para o caracter 30 (começando em 0)
    print(arquivo.readlines())

#arquivo.close() # Não necessita, pois o arquivo já foi fechado