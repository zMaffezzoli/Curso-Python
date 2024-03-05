from math import factorial

def cosseno_hiperbolico_angulo(angulo):
    pi = 3.141593
    angulo_radiano = angulo * (pi/180)
    cosseno_angulo = 0
    
    for i in range(6):
        cosseno_angulo += (angulo_radiano ** (2 * i)) / factorial(2*i)
            
    return cosseno_angulo

print(cosseno_hiperbolico_angulo(90))
print(cosseno_hiperbolico_angulo(180))
print(cosseno_hiperbolico_angulo(220))