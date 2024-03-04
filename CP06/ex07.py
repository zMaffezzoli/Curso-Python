soma = 0

for i in range(10):
    valor = int(input("Digite um valor: "))

    if valor < 0:
        continue

    soma += valor

print(soma/10)