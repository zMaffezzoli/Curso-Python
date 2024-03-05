from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "arq.txt")

escrever = "1"
with open(arquivotxt, mode="w", encoding='UTF-8') as arquivo:
    while escrever != "0":
        escrever = input("Digite algo(Para sair digite '0'): ")
        if escrever != "0":
            arquivo.write(escrever + '\n')

with open(arquivotxt, mode="r", encoding='UTF-8') as arquivo:
    texto = arquivo.read()
    for i in texto:
        print(i)