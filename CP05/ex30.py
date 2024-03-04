valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))
valor3 = float(input('Digite um valor: '))

menor = 0
meio = 0
maior = 0

if valor1 >= valor2 and valor1 >= valor3:
    maior = valor1

    if valor2 >= valor3:
        meio = valor2
        menor = valor3

    else:
        meio = valor3
        menor = valor2

elif valor2 >= valor1 and valor2 >= valor3:
    maior = valor2

    if valor1 >= valor3:
        meio = valor1
        menor = valor3

    else:
        meio = valor3
        menor = valor1

elif valor3 >= valor1 and valor3 >= valor2:
    maior = valor3

    if valor1 >= valor2:
        meio = valor1
        menor = valor2

    else:
        meio = valor2
        menor = valor1

print(menor, meio, maior)