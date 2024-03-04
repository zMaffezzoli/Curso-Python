lista = []

numero = 0
while len(lista) != 100:

    if numero % 7 or str(numero)[-1] == "7":
        lista.append(numero)
        numero += 1

    else:
        numero += 1

print(lista)