from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt1 = path.join(caminho, "texto1.txt")
arquivotxt2 = path.join(caminho, "texto2.txt")
arquivotxt3 = path.join(caminho, "texto3.txt")

try:

    arquivo1 = open(arquivotxt1, mode="r", encoding='UTF-8')
    conteudo_arquivo1 = arquivo1.read()
        
    arquivo2 = open(arquivotxt2, mode="r", encoding="utf-8")
    conteudo_arquivo2 = arquivo2.read()

    with open(arquivotxt3, mode="w", encoding="utf-8") as arquivo3:
        arquivo3.write(conteudo_arquivo1 + conteudo_arquivo2)

    arquivo1.close()
    arquivo2.close()

except Exception as err:
    print(f"Não foi possível ler os arquivos e criar outro, erro: {err}")