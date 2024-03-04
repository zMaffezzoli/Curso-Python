comeco = int(input("Digite um valor de início: "))
final = int(input("Digite um valor final: "))

soma = 0
multiplicacao = 1

for i in range(comeco, final+1):

    if not i % 2:
        soma += i

    else:
        multiplicacao *= i


print(f"Soma dos números pares {soma}, multiplicação dos números ímpares {multiplicacao}")