x = int(input('Digite um valor: '))
y = int(input('Digite um valor: '))
z = int(input('Digite um valor: '))

operacao = input('\n(a) Geométrica \n(b) Ponderada \n(c) Harmônica \n(d) Aritmética \nDigite a operação desejada: ')

match operacao:

    case 'a':
        print(f'Geométrica: {(x * y * z)**(1 / 3)}')

    case 'b':
        print(f'Ponderada: {(x + 2*y + 3*z)/6}')

    case 'c':
        print(f'Harmônica: {1 / (1/x) + (1/y) + (1/z)}')
    
    case 'd':
        print(f'Aritmética: {(x + y + z) / 3}')

    case _:
        print('Opção não existe')