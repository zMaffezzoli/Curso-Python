def equacao(valor):
    soma = 0

    for i in range(1, valor + 1):
        soma += ((i**2) + 1) / (i + 3)

    return soma

print(equacao(1))
print(equacao(2))
print(equacao(3))