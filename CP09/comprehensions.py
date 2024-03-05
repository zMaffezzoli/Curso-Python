lista = [i for i in range(1, 6)]

pares = [i for i in lista if i % 2 == 0]

dicionario = {i: ('par' if i % 2 == 0 else 'impar') for i in lista}

print(dicionario)