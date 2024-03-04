lista = []

for i in range(10):
    valor = int(input("Digite um valor: "))

    lista.append(valor)


print(f"Maior: {max(lista)}. Menor: {min(lista)}")