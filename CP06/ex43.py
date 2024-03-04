idades = 0
qtd_pessoas = 0

while True:

    idade = int(input("Digite uma idade: "))

    if idade == 0:
        break

    else:
        idades += idade
        qtd_pessoas += 1

print(f"Média de idade é: {idades/qtd_pessoas}")