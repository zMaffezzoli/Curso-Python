valor = int(input("Digite um valor: "))

sequencia1 = 0
sequencia2 = 0
sequencia3 = 0

for i in range(1, valor+1):
    sequencia1 += i

for i in range(1, valor+1):
    
    if not i % 2:
        sequencia2 += i * -1

    else:
        sequencia2 += i

for i in range(1, valor+1, 2):
    sequencia3 += i

print(sequencia1, sequencia2, sequencia3)