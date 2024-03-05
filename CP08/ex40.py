def conta_par(numeros):
    pares = []

    for i in numeros:
        if i % 2 == 0:
            pares.append(i)

    return len(pares)


print(conta_par([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(conta_par([20, 22, 23]))