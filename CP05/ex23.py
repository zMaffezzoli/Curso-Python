ano = int(input('Digite um ano: '))

if not ano % 4 and ano % 100:
    print('É divisível')

else: 
    print('Não é divisivel')