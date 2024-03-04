valor = int(input("Digite um valor: "))

for i in range(1, valor+1):
    if not i % 11 or not i % 13 or not i % 17:
        print(i)
        break