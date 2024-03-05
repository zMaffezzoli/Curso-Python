pessoas = [("Pedro", 10), ("Aline", 19), ("Bianca", 12)]

pessoas.sort(key=lambda x: x[1])
print(pessoas)

# SORTED é a mesma coisa que sort(), porém sort é um método exclusivo para listas
# sorted é usado para outros interáveis