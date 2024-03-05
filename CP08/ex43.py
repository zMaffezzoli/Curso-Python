from random import randint

def adiciona_aleatorio(numeros):
    
    for i in range(10):
        numero = randint(1, 100)
        if numero not in numeros:
            numeros.append(numero)


    return numeros

print(adiciona_aleatorio([1, 2, 3]))
print(adiciona_aleatorio([69, 39, 51]))