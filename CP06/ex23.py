valor = int(input("Digite um valor: "))

print(f"Divisores de {valor}: ", end="")

for i in range(1, valor+1):
    if not valor % i:
        print(i , end=" ")