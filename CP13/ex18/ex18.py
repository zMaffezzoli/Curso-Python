from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "lista.txt")

try: 

    with open(arquivotxt, mode="r", encoding="UTF-8") as arquivo:

        total = 0
        linhas = arquivo.readlines()

        for i in linhas:
            total += float(i[i.index("$") + 1:])

        print(f"O total da compra é de R${total}")
        
except Exception as err:
    print(f"Não foi possível ler o arquivo, erro: {err}")