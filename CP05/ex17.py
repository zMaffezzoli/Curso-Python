base_menor = float(input('Digite a base menor do trapézio: '))
base_maior = float(input('Digite a base maior do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

if base_maior <= 0 or base_menor <= 0 or altura <= 0:
    print("Valor inválido!")

else:
    area = (base_maior + base_menor) * altura / 2
    print(f'Área do trapézio: {area}')