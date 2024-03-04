lista1 = list(range(1, 51))

lista2 = []

for i in lista1:
    lista2 += [(i+5*i)%(i+1)]


print(lista2)