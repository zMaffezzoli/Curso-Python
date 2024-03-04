"""
Funções de maior grandeza (Higher Order Functions) - HOF
# São funções que retornam outras funções
"""

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcula(num1, num2, funcao):
    return funcao(num1, num2)


print(calcula(8, 4, somar))

print(calcula(8, 4, diminuir))

print(calcula(8, 4, multiplicar))

print(calcula(8, 4, dividir))