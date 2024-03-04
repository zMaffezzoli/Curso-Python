import timeit, functools

def teste(n):
    soma = 0
    for i in range(n):
        soma += 1

    return soma

#Tempo que a execução levou para fazer a função com parametro 10 10000000 vezes
print(timeit.timeit(functools.partial(teste, 10), number=10000000))