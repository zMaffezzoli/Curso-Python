valor_produto = float(input("Digite o valor do produto: "))

if valor_produto <= 50:
    valor_produto *= 1.05

elif valor_produto >= 50 and valor_produto <= 100:
    valor_produto *= 1.10

else:
    valor_produto *= 1.15

if valor_produto <= 80:
    print(f"Barato, preço está {valor_produto}")

elif valor_produto >= 80 and valor_produto <= 120:
    print(f"Normal, preço está {valor_produto}")

elif valor_produto >= 120 and valor_produto <= 200:
    print(f"Caro, preço está {valor_produto}")

else:
    print(f'Muito caro, preço está {valor_produto}')