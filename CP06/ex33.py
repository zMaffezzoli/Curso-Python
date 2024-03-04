divisivel1 = int(input("Digite um numero: "))
divisivel2 = int(input("Digite um numero: "))
qtd_numeros = int(input(f"Digite a quantidade de números divisiveis por {divisivel1} e {divisivel2}: "))

qtd_divisiveis = 0

numero = 0

while qtd_divisiveis < qtd_numeros:

    if not (numero % divisivel1) or not(numero % divisivel2):
        qtd_divisiveis += 1
        print(numero)
        numero += 1

    else:
        numero +=1

