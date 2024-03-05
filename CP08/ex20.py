def fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial

print(fatorial(5))
print(fatorial(6))
print(fatorial(7))