habitantes = 10
kwh = 0.55

consumo1 = 0
consumo2 = 0
consumo3 = 0

consumo_media = 0

maior = 0
menor = 0

for i in range(habitantes):

    consumo = float(input("Digite o consumo de energia em um mês: "))

    consumo *= 0.55

    consumo_media += consumo

    if i == 0:
        maior = consumo
        menor = consumo

    if consumo > maior:
        maior = consumo

    if consumo < menor:
        menor = consumo

    cod = int(input("Digite o código do consumidor(1-Residencial, 2-Comercial, 3-Industrial): "))

    if cod == 1:
        consumo1 += consumo

    elif cod == 2:
        consumo2 += consumo

    elif cod == 3:
        consumo3 += consumo

print(f"O maior consumo foi R${maior}, o menor R${menor}, a media R${consumo_media/habitantes}")
print(f"Categoria 1-Residencial: {consumo1}")
print(f"Categoria 2-Comercial: {consumo2}")
print(f"Categoria 3-Industrial: {consumo3}")