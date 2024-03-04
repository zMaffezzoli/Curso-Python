km = float(input('Digite a distância percorrida: '))
litros = float(input('Litros de gasolina consumidos: '))

consumo = km / litros

if consumo < 8:
    print('Venda o carro!')

elif consumo >= 8 and consumo <= 14:
    print('Econômico!')

else:
    print('Super econômico')