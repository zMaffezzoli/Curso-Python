print('Especificação | Código | Preço')
print('Cachorro quente | 100  | 1,20')
print('Bauru simples | 101    | 1,30')
print('Bauru com ovo | 102    | 1,50')
print('Hamburguer    | 103    | 1,20')
print('Cheeseburguer | 104    | 1,70')
print('Suco          | 105    | 2,20')
print('Refrigerante  | 106    | 1,00\n')

produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade deste item: "))

match produto:

    case 100:
        print(f'Valor: R${quantidade*1.20}')

    case 101:
        print(f'Valor: R${quantidade*1.30}')

    case 102:
        print(f'Valor: R${quantidade*1.50}')

    case 103:
        print(f'Valor: R${quantidade*1.20}')

    case 104:
        print(f'Valor: R${quantidade*1.70}')

    case 105:
        print(f'Valor: R${quantidade*2.20}')

    case 106:
        print(f'Valor: R${quantidade*1}')