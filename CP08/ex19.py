from math import sqrt
 
def maior_fator_primo(numero):
     
    maior_primo = -1
     
    while numero % 2 == 0:
        maior_primo = 2
        numero /= 2
         
    while numero % 3 == 0:
        maior_primo = 3
        numero = numero / 3
     
    for i in range(5, int(sqrt(numero)) + 1, 6):

        while numero % i == 0:
            maior_primo = i
            numero = numero / i

        while numero % (i+2) == 0:
            maior_primo = i + 2
            numero = numero / (i+2)
         
    if numero > 4:
        maior_primo = numero
     
    return int(maior_primo)
 
print(maior_fator_primo(15))
print(maior_fator_primo(49))