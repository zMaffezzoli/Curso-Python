from random import randint

lista = list(randint(-10, 10) for i in range(10))

positivos = 0
negativos = 0

for i in lista:
    if i >= 0:
        positivos += i

    else:
        negativos += 1

print(lista)
print(f"Soma positivos: {positivos}. Quantidade Negativos: {negativos}")