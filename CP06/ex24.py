valor = int(input("Digite um valor: "))
soma = 0

for i in range(1, valor):
    if not valor % i:
        soma += i



print(f"Soma dos divisores de {valor}: {soma}")