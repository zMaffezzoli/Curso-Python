from random import randint

vetor = list(randint(1, 100) for i in range(10))
print(vetor)

vetor.sort()
print(vetor)