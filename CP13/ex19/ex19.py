from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "alunos.txt")

try: 

    with open(arquivotxt, mode="r", encoding="UTF-8") as arquivo:

        maior = -1
        pessoa = ""
        linhas = arquivo.readlines()

        for i in linhas:
            if (int(i[(i.index("NOTA:") + 6):-1])) >= maior:
                maior = int(i[(i.index("NOTA:") + 6):-1])
                pessoa = i[(i.index("NOME: ") + 6):-1]

        print(f"{pessoa}")
        
except Exception as err:
    print(f"Não foi possível ler o arquivo, erro: {err}")