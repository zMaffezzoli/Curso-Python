from math import gcd

numero = 1

for i in range(2, 11):
    numero = numero * i // gcd(numero, i)

print(numero)