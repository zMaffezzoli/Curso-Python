from math import sqrt

valor = float(input("Digite um valor: "))

if valor >= 0:
    print(f"A raíz de {valor} é {sqrt(valor)}")
    
else:
    print(f"O valor é inválido!")