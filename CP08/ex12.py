def soma_algarismos(numero=251):
    total = 0
    lista = list(str(numero))
    for i in lista:
        total += int(i)

    return total


print(soma_algarismos())
print(soma_algarismos(111))