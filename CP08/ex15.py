def triangulo(lado1, lado2, lado3):

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

        if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
            return f"Triângulo equilátero"
        
        elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
            return f"Triângulo escaleno"
        
        return f"Triângulo isósceles"

    return "Não é triângulo"

print(triangulo(5, 5, 3))
print(triangulo(1, 1, 1))
print(triangulo(2, 5, 6))
print(triangulo(1, 100, 50))