numero = 0
for j in range(999, 99, -1):

    for i in range(999, 99, -1):

        temporario = str(i * j)
        temp_inverso = temporario[::-1]

        if temporario == temp_inverso:
            numeroTemp = int(temporario)

            if numeroTemp > numero:
                numero = numeroTemp


print(numero)