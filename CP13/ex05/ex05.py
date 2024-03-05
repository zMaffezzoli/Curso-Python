from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

try:
    with open(arquivotxt, mode="r", encoding='UTF-8') as arquivo:
        conteudo_arquivo = arquivo.read()

        caractere = input("Qual caractere deseja contar: ")

        print(f"O caractere {caractere} aparece {conteudo_arquivo.count(caractere)} vezes no arquivo")

except Exception as err:
    print(f"Não foi possível ler quantos caracteres o arquivo tem, erro: {err}")