def fracao(numerador, denominador):
    return numerador, denominador

def divisor_comum(numerador, denominador):
    lista = [numerador, denominador]

    for i in range(1, max(lista)):
        if numerador % i == 0 and denominador % i == 0:
            numerador = numerador / i
            denominador = denominador / i

    return numerador, denominador

def operacoes(numerador_fracao1, denominador_fracao1, numerador_fracao2, denominador_fracao2):
    fracao1 = numerador_fracao1 / denominador_fracao1
    fracao2 = numerador_fracao2 / denominador_fracao2
    soma = fracao1 + fracao2
    subtracao = fracao1 - fracao2
    produto = fracao1 * fracao2
    quociente = fracao1 / fracao2

    return soma, subtracao, produto, quociente

p = fracao(50, 25)
q = fracao(25, 5)

print(p)
print(q)
print(divisor_comum(p[0], p[1]))
print(divisor_comum(q[0], q[1]))
print(operacoes(numerador_fracao1=p[0], denominador_fracao1=p[1], numerador_fracao2=q[0], denominador_fracao2=q[1]))