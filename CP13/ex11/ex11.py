from os import path

caminho = path.dirname(path.abspath(__file__))

try:
    arquivo = input("Informe o nome do arquivo (com a extensão): ")
    arquivotxt = path.join(caminho, arquivo)
    palavra = input("Digite a palavra que você deseja contar no arquivo: ")

    with open(arquivotxt, mode='r', encoding='UTF-8') as arquivo:
        conteudo_arquivo = arquivo.read()

        print(f"A palavra '{palavra}' aparece {conteudo_arquivo.count(palavra)} vezes no arquivo")

except Exception as err:
    print(f"Não foi possível ler o arquivo e criar outro, erro: {err}")