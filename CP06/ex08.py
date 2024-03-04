maior = 0
menor = 0

for i in range(10):
    valor = float(input("Digite um valor: "))

    if i == 0:
        maior = valor
        menor = valor

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print(f"O menor é {menor}, o maior é {maior}")