from random import uniform

lista = list (uniform(1, 10) for i in range(15))

for i in range(len(lista)):
    lista[i] = float(f"{lista[i]:.2f}")

print(f"A média foi: {sum(lista)/len(lista)}")