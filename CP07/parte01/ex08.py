from random import randint

lista = list(randint(1, 20) for i in range(6))

print(lista)
lista.reverse() # Ou lista[::-1]
print(lista)