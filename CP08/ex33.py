from math import factorial

def soma_algarismos(numero):
    fatorial = factorial(numero)
    soma_fatorial = 0

    for i in str(fatorial):
        soma_fatorial += int(i)
    
    return soma_fatorial

print(soma_algarismos(4))
print(soma_algarismos(5))
print(soma_algarismos(6))