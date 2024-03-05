from math import sqrt

def desvio_padrao(vetor):
    media = sum(vetor) / len(vetor)

    desvio = 0

    for i in vetor:
        desvio += (i - media)**2

    return sqrt(desvio / len(vetor))


print(desvio_padrao((7, 9, 10, 11, 13)))
print(desvio_padrao((1, 2, 3, 4, 5)))