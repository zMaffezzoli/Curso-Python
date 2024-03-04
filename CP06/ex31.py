denominador = 1

resultado = 0

for i in range(1, 100, 2):
    resultado += i / denominador
    print(i, denominador)
    denominador += 1

print(resultado)