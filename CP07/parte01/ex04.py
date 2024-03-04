from random import randint

lista = list(randint(1, 20) for i in range(8))

x = int(input("Digite o valor do indice a ser somado: "))
y = int(input("Digite o valor do outro indice a ser somado: "))

print(lista)
print(f"A soma dos indices{x} e {y} é {lista[x-1] + lista[y-1]}")