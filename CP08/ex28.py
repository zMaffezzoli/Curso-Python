from math import factorial

def cosseno_angulo(angulo):
    cosseno_angulo = 0
    pi = 3.141593
    angulo_radiano = angulo * (pi/180)

    for i in range(6):
        if i % 2 == 1:
            cosseno_angulo += ((-1 ** i) / (factorial(2*i))) * (angulo_radiano ** (2*i))

        else:
            cosseno_angulo -= ((-1 ** i) / (factorial(2*i))) * (angulo_radiano ** (2*i))
            
    return cosseno_angulo

print(cosseno_angulo(15))
print(cosseno_angulo(30))
print(cosseno_angulo(60))