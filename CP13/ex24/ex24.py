from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "mercadorias.txt")

try:
    arquivo = open(arquivotxt, mode="w+", encoding="UTF-32")
        
    while True:
        cod = input("Digite o código do produto (Para parar de adicionar digite '0'): ")

        if cod == "0":
            break

        desc = input("Digite a descrição do produto: ")
        qtd = input("Digite a quantidade desse produto: ")

        arquivo.write(f"{cod} - {desc} / {qtd}\n")


    arquivo.seek(0)
    print(f"Produtos disponíveis: \n")
    print(arquivo.read())
    arquivo.seek(0)
    armazena = arquivo.readlines()
    arquivo.close()

    arquivo = open(arquivotxt, mode="w+", encoding="UTF-32")
    indisponiveis = []

    while True:
        excluir = input("Digite o COD do produto que deseja excluir: (Para parar digite '0'): ")

        if excluir == "0":
            for i in armazena:
                arquivo.write(i)
            break

        indice = 0
        for i in armazena:
            if excluir in i:
                indisponiveis.append(i[0 : i.index("-") - 1])
                armazena.pop(indice)
            else:
                indice += 1

    arquivo.seek(0)
    print(f"Produtos disponíveis: \n")
    print(arquivo.read())
    arquivo.close()
    for i in indisponiveis:
        print(f"Produto: {i} indisponível\n")

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")