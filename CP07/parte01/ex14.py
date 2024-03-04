from random import randint
from collections import Counter

lista = list(randint(1, 20) for i in range(10))

print(lista)
verificando = Counter(lista)

for chave, valor in verificando.items():
    if valor != 1:
        print(f"{chave} Repete {valor} vezes")

    else:
        pass