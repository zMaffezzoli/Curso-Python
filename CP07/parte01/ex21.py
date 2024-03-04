from random import randint

a = list(randint(1, 20) for i in range(10))
b = list(randint(1, 20) for i in range(10))

c = []

for i in range(len(a)):
    c += [a[i] - b[i]]


print(a)
print(b)
print(c)