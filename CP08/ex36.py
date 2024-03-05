def super_fatorial(numero):
    lista = list(range(numero, 0, -1))
    fatorial = 1

    for i in lista:
        for j in range(1, i + 1):
            fatorial *= j

    return fatorial

print(super_fatorial(4))
print(super_fatorial(5))
print(super_fatorial(6))