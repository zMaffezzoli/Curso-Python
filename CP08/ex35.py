def fatorial_quadruplo(numero):
    numerador = 1
    denominador = 1

    for i in range(1, (numero * 2) + 1):
        numerador *= i

    for i in range(1, numero + 1):
        denominador *= i

    return (numerador/denominador)

print(fatorial_quadruplo(5))
print(fatorial_quadruplo(6))
print(fatorial_quadruplo(7))