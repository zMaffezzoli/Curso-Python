from random import randint

lista = list(randint(1, 20) for i in range(10))

print(lista)
print(f"Maior elemento: {max(lista)}. Seu indice(Programação): {lista.index(max(lista))}. Sua posição: {lista.index(max(lista)) + 1}")