valor_produto = float(input('Digite o valor do produto: '))
estado = input('Digite o estado(MG/SP/RJ/MS): ')
estado = estado.upper()

match estado:
    case 'MG':
        print(f'Preço do produto com imposto R${valor_produto * 1.07}')

    case 'SP':
        print(f'Preço do produto com imposto R${valor_produto * 1.12}')

    case 'RJ':
        print(f'Preço do produto com imposto R${valor_produto * 1.15}')

    case 'MS':
        print(f'Preço do produto com imposto R${valor_produto * 1.08}')

    case _:
        print('Erro! Estado não está na lista')