valor = 1
contador = 0

while True:
    if not (valor % 3):
        contador += 1
        print(valor)

    if contador == 5:
        break

    valor += 1