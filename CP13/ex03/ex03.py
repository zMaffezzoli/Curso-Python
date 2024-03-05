from os import path
from collections import Counter

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "texto.txt")

try:
    with open(arquivotxt, mode="r", encoding='UTF-8') as arquivo:
        texto = arquivo.read()
        contador = Counter(texto)
        
        vogais = contador['a'] + contador['A'] + contador['e'] + contador['E'] + contador['i'] + contador['I'] + contador['o'] + contador['O'] + contador['u'] + contador['U']
        print(f"{vogais} são vogais")
    
except Exception as err:
    print(f"Não foi possível ler quantas vogais o arquivo tem, erro: {err}")