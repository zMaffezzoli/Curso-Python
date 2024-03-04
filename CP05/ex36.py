valor_venda = float(input("Digite o valor da venda: "))

if valor_venda >= 100_000:
    print(f'O valor da comissão será de: R${700 + valor_venda*0.16}')

elif valor_venda <= 100_000 and valor_venda >= 80_000:
    print(f'O valor da comissão será de: R${650 + valor_venda*0.14}')

elif valor_venda <= 80_000 and valor_venda >= 60_000:
    print(f'O valor da comissão será de: R${600 + valor_venda*0.14}')

elif valor_venda <= 60_000 and valor_venda >= 40_000:
    print(f'O valor da comissão será de: R${550 + valor_venda*0.14}')

elif valor_venda <= 40_000 and valor_venda >= 20_000:
    print(f'O valor da comissão será de: R${500 + valor_venda*0.14}')

else:
    print(f'O valor da comissão será de: R${400 + valor_venda*0.14}')