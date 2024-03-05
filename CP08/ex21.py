def quantidade_primos(numero):
    
    numeros = list(range(numero))
    soma_primos = 0

    for i in numeros:
        if i > 1:
            for j in range(2, i):
        
                if (i % j) == 0:
                    break
                
            else:
                soma_primos += 1
    
    return soma_primos
        
print(quantidade_primos(5))
print(quantidade_primos(7))
print(quantidade_primos(11))