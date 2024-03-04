vetor1 = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0]

for i in vetor1:

    if i == 0:
        vetor1.pop(vetor1.index(i))

print(vetor1)