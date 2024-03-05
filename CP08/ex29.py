from math import factorial

def seno_hiperbolico_angulo(angulo):
    pi = 3.141593
    angulo_radiano = angulo * (pi/180)
    seno_angulo = 0
    
    for i in range(6):
        seno_angulo += (angulo_radiano ** (2 * i + 1)) / factorial(2*i + 1)
            
    return seno_angulo

print(seno_hiperbolico_angulo(90))
print(seno_hiperbolico_angulo(180))
print(seno_hiperbolico_angulo(220))