def par_impar(vetor):
    pares = []
    impares = []

    for i in vetor:
        if i % 2 == 0:
            pares.append(i)

        else:
            impares.append(i)

    return pares, impares

print(par_impar(list(range(1, 31))))
print(par_impar(list(range(30, 61))))