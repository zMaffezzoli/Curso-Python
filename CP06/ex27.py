valor = int(input("Digite um valor para a série harmónica: "))

harmonica = 0
for i in range(1, valor+1):
    harmonica += 1/i

print(harmonica)