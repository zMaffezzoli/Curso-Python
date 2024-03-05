def somatorio(numero):
    soma = 0

    for i in range(1, numero+1):
        soma += i

    return soma

print(somatorio(5))
print(somatorio(6))