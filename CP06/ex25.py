soma = 0

for i in range(1, 1000):
    if (not i % 3) or (not i % 5):
        soma += i

print(soma)