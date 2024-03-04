lista = []

qtd_numeros = 5
for i in range(qtd_numeros):
    valor = float(input("Digite um valor: "))

    lista.append(valor)

print(lista)
print(f"Maior: {max(lista)}. Menor {min(lista)}. Média: {sum(lista)/len(lista)} ")