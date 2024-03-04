qtd_valores = 0
pares = 0
valor = 999

while valor != 1000:
    valor = int(input("Digite um número diferente de 1000: "))

    qtd_valores += 1

    if not valor % 2:
        pares += 1


print(f"Foi informado {qtd_valores} números e {pares} eram pares")