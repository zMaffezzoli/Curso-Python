from collections import defaultdict

dicionario = {"a": 1, "b": 2, "c": 3}

print(dicionario.get("e"))

#print(dicionario["e"]) # Apresenta erro! (KeyError) em dicionário comum

dicionario2 = defaultdict(lambda: 0)

dicionario2.update({"a": 1, "b": 2})

print(dicionario2)

print(dicionario2['c']) # Em vez de dar erro, cria a chave com um valor padrão
print(dicionario2)