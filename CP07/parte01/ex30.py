from random import randint

vetor1 = list(randint(1, 100) for i in range(10))
vetor2 = list(randint(1, 100) for i in range(10))

interseccao = set(vetor1).intersection(set(vetor2))

print(vetor1)
print(vetor2)
print(interseccao)