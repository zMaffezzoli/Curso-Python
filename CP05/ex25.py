from math import sqrt

print('Digite somente os números para a equação de 2º grau (ax² + bx + c = 0)')

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a != 0:
    delta = sqrt(b**2 - 4 * a * c)

    if delta < 0:
        print('Não existe raiz')

    elif delta == 0:
        raiz_unica = (- b + delta) / (2 * a)
        print(f'Raiz única: {raiz_unica}')

    else:
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        print(f'S = ({x1},{x2})')

else:
    print('Não é equação de segundo grau')