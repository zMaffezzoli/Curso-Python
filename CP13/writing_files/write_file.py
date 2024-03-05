from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

escrever = "1"
with open(arquivotxt, mode="a+", encoding='UTF-8') as arquivo: # Irá apagar o outro arquivo e criar um novo, mesmo se já existente
    while escrever != "sair":
        escrever = input("Digite algo(Para sair digite 'sair'): ")
        if escrever != "sair":
            arquivo.write(escrever)
            arquivo.write('\n')
        