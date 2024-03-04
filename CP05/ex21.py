operacao = int(input('1- Soma de 2 números \n2- Diferença entre 2 números (maior pelo menor) \n3- Produto entre 2 números \n4- Divisão entre 2 números (o denominador não pode ser zero) \n'))

if operacao <= 0 or operacao > 4:
    print('Opção inválida!')

else:
    valor1 = float(input('Digite um número: '))
    valor2 = float(input('Digite outro número: '))

    match operacao:

        case 1:
            print(f'Soma: {valor1 + valor2}')

        case 2:
            if valor1 > valor2:
                print(f'{valor1 - valor2}')

            else: 
                print(valor2 - valor1)

        case 3:
            print(f'Produto: {valor1 * valor2}')

        case 4:
            if valor2 == 0:
                print('Denominador não pode ser 0!')

            else:
                print(f'Divisão: {valor1 / valor2}')