from math import factorial

def seno_angulo(angulo):
    seno_angulo = 0
    pi = 3.141593
    angulo_radiano = angulo * (pi/180)

    for i in range(6):
        if i % 2 == 1:
            seno_angulo += ((-1 ** i) / (factorial(2*i + 1))) * (angulo_radiano ** (2*i + 1))

        else:
            seno_angulo -= ((-1 ** i) / (factorial(2*i + 1))) * (angulo_radiano ** (2*i + 1))
            
    return seno_angulo

print(seno_angulo(15))
print(seno_angulo(30))
print(seno_angulo(90))