from math import factorial

def neperiano(numero):
    numero_neperiano = 0

    for i in range(numero+1):
        numero_neperiano += 1 / factorial(i)

    return numero_neperiano

print(neperiano(1))
print(neperiano(2))
print(neperiano(3))