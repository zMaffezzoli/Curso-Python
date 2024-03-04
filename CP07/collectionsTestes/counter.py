from collections import Counter

palavra = "eu sou eu e acontece que eu sou eu"

qtd_letras = Counter(palavra)

qtd_palavras = Counter(palavra.split())

# 5 palavras com mais ocorrencia
print(qtd_palavras.most_common(5))