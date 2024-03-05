"""def soma(x, y):
    return x + y
"""
soma = lambda x, y: x + y       #lamba é uma função sem nome

print(soma(2,5))

pessoas = ["Robert Kanye", "William Adams", "Anderson Bob"]

# Sort por sobrenome
pessoas.sort(key=lambda sobrenome: sobrenome.split(' ')[-1]) 
print(pessoas)

# lamda dados: dados[0], dado[1] + 1
# Mantem os dados no primeiro indice e altera os do 2 indice