paises = {
        "br": "Brasil",
        "eua": "Estados Unidos",  # Dicionarios permitem qualquer valor, tanto na chave qunato no valor
        "py": "Paraguai"
}

# Retorna None caso não encontrado
print(paises.get("br")) # Recomendado, porém também funciona assim => paises["br"] // Caso não encontrado retorna error

print(paises.get("ru", "País não encontrado")) # Segundo parametro é para caso não encontre // Caso não informado retorna None == False

#print("br" in paises)
#print("Estados Unidos" in paises)

paises["ru"] = "Russia" # paises.update({}"ru": "Russia"}) <== também funciona // Tanto para criar ou alterar valores

print(paises)

paises.pop("ru") # del paises["ru"]
print(paises)

# Listas e dicionarios possuem Shallow Copy, tuplas não (IMUTÁVEIS!)

for chave in paises.keys():    # Acessar chaves 
    print(chave)

for valores in paises.values(): # Acessar valores
    print(valores)

for chave, valor in paises.items(): # Acessar ambos
    print(chave, valor)


dicionario = {}.fromkeys([1, 2, 3, 4, 5], "dict")
print(dicionario)