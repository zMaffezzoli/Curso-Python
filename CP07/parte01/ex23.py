from random import randint

conjunto1 = [1, 5, 8, 15, 19]
conjunto2 = [2, 18, 26, 34, 9]
escalar = 0

for i in range(len(conjunto1)):

    escalar += conjunto1[i] * conjunto2[i]

print(conjunto1)
print(conjunto2)
print(escalar)