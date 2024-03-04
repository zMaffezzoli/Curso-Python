from math import factorial

valor = int(input("Digite um valor: "))
resultado = 1

for i in range(1, valor+1):
    resultado += 1/(factorial(i))
    print(resultado)

print(resultado)