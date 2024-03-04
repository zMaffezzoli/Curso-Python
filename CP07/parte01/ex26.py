from random import randint
from math import sqrt

vetor = list(randint(1, 20) for i in range(10))
media_vetor = sum(vetor) / (len(vetor))

primeira_parte = 1 / (len(vetor) - 1)

segunda_parte = 0

for i in vetor:
    segunda_parte += (i - media_vetor)**2

final = primeira_parte*segunda_parte
print(vetor)
print(sqrt(final))