def fatorial_exponencial(numero):
    for i in range(numero-1, 0, -1):
        numero = numero ** i

    return numero

print(fatorial_exponencial(4))
print(fatorial_exponencial(5))