valor_a = float(input("Digite o lado A do triângulo: "))
valor_b = float(input("Digite o lado B do triângulo: "))
valor_c = float(input("Digite o lado C do triângulo: "))


if (valor_a + valor_b < valor_c) or (valor_a + valor_c < valor_b) or (valor_c + valor_b < valor_a):
    print('Não pe um triângulo')
          
else:
    if valor_a == valor_b and valor_b == valor_c:
        print('Triângulo equilátero')

    elif valor_a == valor_b or valor_b == valor_c or valor_c == valor_a:
        print('Triângulo isósceles')

    else:
        print('Triângulo escaleno')