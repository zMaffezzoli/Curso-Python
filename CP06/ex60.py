soma = 0
qtd_digitados = 0

numeros = []
pares = 0
qtd_pares = 0

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    soma += numero
    qtd_digitados += 1
    numeros.append(numero)

    if not numero % 2:
        pares += numero
        qtd_pares +=1

    else:
        pass

print(f"Soma: {soma} Quantidade: {qtd_digitados} Média: {soma/qtd_digitados} Menor: {min(numeros)} Maior: {max(numeros)} Media números pares: {pares/qtd_pares}")