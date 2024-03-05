from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "cadastro.txt")

telefone = "1"
try:

    with open(arquivotxt, mode="w", encoding="UTF-8") as arquivo:
        
        while telefone != "0":

            nome = input("Digite o nome a ser cadastrado: ")
            telefone = input("Digite o telefone dessa pessoa: ")

            if telefone != "0":
                arquivo.write(nome + ":" + " " + telefone)
                arquivo.write("\n")


except Exception as err:
    print(f"Não foi possível realizar os cadastros no arquivo, erro: {err}")