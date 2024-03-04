fibonacci = [0, 1]

soma = 0

for i in range(33):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for i in fibonacci:
    if i > 4_000_000:
        break

    else:
        if not(i%2):
            soma += i
print(soma)