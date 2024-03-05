def triangulo(altura):
    espaco_branco = 2*altura
    
    for i in range(1, 2*altura, 2):
        print(" "* espaco_branco + "*" * i)
        espaco_branco -= 1

triangulo(5)
print()
triangulo(6)
print()
triangulo(7)