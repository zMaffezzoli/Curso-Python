from os import path

caminho = path.dirname(path.abspath(__file__))

arquivotxt = path.join(caminho, "texto.txt")
arquivo = open(arquivotxt) # Por padrão a abertura é em mode r (read)

print(list(arquivo))

arquivo.close()