maior = 0
menor = 0

controlador = 1

while True:

    valor = float(input("Digitte um número: "))

    if controlador == 1:
        maior = valor
        menor = valor
        controlador += 1

    elif valor < 0:
        break

    else:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

print(f"Maior: {maior} Menor: {menor}")