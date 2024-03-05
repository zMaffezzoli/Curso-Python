from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt1 = path.join(caminho, "texto1.txt")
arquivotxt2 = path.join(caminho, "texto2.txt")

vogais = "AEIOUaeiou"

try:
    with open(arquivotxt1, mode="r", encoding='UTF-8') as arquivo:
        conteudo_arquivo = arquivo.read()
        novo_texto = ""

        for i in conteudo_arquivo:
            if i not in vogais:
                novo_texto += "*"

            else:
                novo_texto += i

    with open(arquivotxt2, mode="w", encoding="utf-8") as arquivo2:
        arquivo2.write(novo_texto)
            
except Exception as err:
    print(f"Não foi possível ler o arquivo e criar outro, erro: {err}")