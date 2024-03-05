def hiper_fatorial(numero):
    lista = list(range(2, numero+1))
    fatorial = 1

    for i in lista:
        fatorial *= (i**i)

    return fatorial

print(hiper_fatorial(3))
print(hiper_fatorial(4))
print(hiper_fatorial(5))