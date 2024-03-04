numeros = []

while len(numeros) != 10:

    num = int(input("Digite um número>: "))

    if num in numeros:
        print("Digite outro número!")
        continue

    else:
        numeros.append(num)

print(numeros)