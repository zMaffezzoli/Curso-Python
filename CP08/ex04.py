from math import sqrt

def quadrado_perfeito(numero):

    if numero >= 0 and sqrt(numero) == int(sqrt(numero)):
        return f"É perfeito"
    
    return f"Não é perfeito"

print(quadrado_perfeito(1))
print(quadrado_perfeito(4))
print(quadrado_perfeito(9))
print(quadrado_perfeito(25))
print(quadrado_perfeito(3))