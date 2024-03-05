from os import path

caminho = path.dirname(path.abspath(__file__))

arquivotxt2 = path.join(caminho, "texto2.txt")


try:
    nome_arquivo = input("Digite nome do arquivo a ser lido: ")
    #nome_arquivo = "texto1.txt"

    arquivotxt1 = path.join(caminho, nome_arquivo)

    with open(arquivotxt1, mode="r", encoding='UTF-8') as arquivo:
        conteudo_arquivo = arquivo.read()
       
    with open(arquivotxt2, mode="w", encoding="utf-8") as arquivo2:
        arquivo2.write(conteudo_arquivo.upper())

except Exception as err:
    print(f"Não foi possível ler o arquivo e criar outro, erro: {err}")