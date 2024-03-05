def consumo(km, litros):
    consumo = km / litros

    if consumo < 8:
        return "Venda o carro!"
    
    elif consumo >= 8 and consumo <= 12:
        return "Econômico!"
    
    return "Super econômico"

print(consumo(10, 2))
print(consumo(20, 2))
print(consumo(30, 2))