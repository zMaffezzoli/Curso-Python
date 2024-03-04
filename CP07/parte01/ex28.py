from random import randint

lista = list(randint(1, 100) for i in range(1, 11))

vetor_impar = []
vetor_par = []

for i in lista:
    if not(i % 2):
        vetor_par.append(i)

    else:
        vetor_impar.append(i)


print(lista)
print(f"Pares: {vetor_par}")
print(f"Impares: {vetor_impar}")