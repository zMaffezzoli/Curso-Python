def fatorial_duplo(numero=5):
    fatorial = 1

    for i in range(1, numero + 1, 2):
        fatorial *= i

    return fatorial


print(fatorial_duplo(5))
print(fatorial_duplo(7))
print(fatorial_duplo(9))