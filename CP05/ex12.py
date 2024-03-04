from math import log10

numero = int(input("Digite um número: "))

if numero < 0:
    print('Número inválido')
    
else:
    print(f'Logaritmo de {numero} é {log10(numero)}')