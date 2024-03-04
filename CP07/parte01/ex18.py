lista = list(range(1, 11))

multiplos = []

valor = int(input("Digite um valor: "))

for i in lista:
    if not (valor % i):
        multiplos.append(i)

print(f"{valor} é multiplo de {multiplos}")