from random import randint

lista = list(randint(1, 20) for i in range(5))

print(lista)

print(f"Posição maior valor: {lista.index(max(lista)) + 1}")
print(f"Posição menor valor: {lista.index(min(lista)) + 1}")