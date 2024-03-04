operacao = int(input("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\nOperação: "))

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))

match operacao:
    case 1:
        print(valor1 + valor2)

    case 2:
        print(valor1 - valor2)

    case 3:
        print(valor1 / valor2)

    case 4:
        print(valor1 * valor2)

    case _:
        print('Operação inválida')