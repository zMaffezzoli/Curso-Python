def triangulo_lateral(numero):
    ponta_esquerda = list(range(1, numero+1))
    ponta_direita = list(range(numero-1, 0, -1))

    for i in ponta_esquerda:
        print("*" * i)

    for i in ponta_direita:
        print("*" * i)

triangulo_lateral(4)
print()
triangulo_lateral(11)