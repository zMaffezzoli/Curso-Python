from os import path
from collections import Counter

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

try:
    with open(arquivotxt, mode="r", encoding='UTF-8') as arquivo:
        texto = arquivo.read()
        contador = Counter(texto)
        
        vogais = contador['a'] + contador['A'] + contador['e'] + contador['E'] + contador['i'] + contador['I'] + contador['o'] + contador['O'] + contador['u'] + contador['U']
        
        consoantes = 0
        for chave, valor in contador.items():
            if chave.isalpha() and (chave.upper() != "A") and (chave.upper() != "E") and (chave.upper() != "I") and (chave.upper() != "O") and (chave.upper() != "U"):
                consoantes += valor

        print(f"Vogais: {vogais} / Consoantes: {consoantes}")

except Exception as err:
    print(f"Não foi possível ler quantas vogais e consoantes o arquivo tem, erro: {err}")