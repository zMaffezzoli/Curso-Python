soma = 0
contador = 1

for i in range(1, 101):
    if not i % 2:
        print(i ,  contador)
        soma += i
        contador += 1

print(f"A soma dos primeiro 50 números pares é {soma}")