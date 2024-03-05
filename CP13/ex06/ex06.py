from os import path
from collections import Counter

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

try:
    with open(arquivotxt, mode="r", encoding='UTF-8') as arquivo:
        conteudo_arquivo = arquivo.read()
        contador = Counter(conteudo_arquivo)
        print(contador)
        for chave, valor in contador.items():
            if chave.isalpha():
                print(f"A letra {chave} aparece {valor} vezes")

except Exception as err:
    print(f"Não foi possível ler quantos caracteres o arquivo tem, erro: {err}")