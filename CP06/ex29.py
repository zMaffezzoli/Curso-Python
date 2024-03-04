from math import factorial

resultado = 0
termos = 5

for i in range(1, termos+1):
    resultado += i/factorial(i*2)

print(resultado)