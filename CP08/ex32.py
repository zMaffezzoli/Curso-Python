def simplificada(numerador, denominador):
    lista = [numerador, denominador]


    for j in range(max(lista), 1, -1):
        for i in range(max(lista), 1, -1):
            if (numerador / denominador) == (j / i):
                numerador = j
                denominador = i

    print(numerador, denominador)
            
simplificada(36,60)
simplificada(20,15)
simplificada(12,6)