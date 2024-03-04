matriz = [[], [], [], []]

for linha in range(1, 5):
    for coluna in range(1, 5):
        if len(matriz[0]) < 4:
            matriz[0].append(linha * coluna)

        elif len(matriz[1]) < 4:
            matriz[1].append(linha * coluna)

        elif len(matriz[2]) < 4:
            matriz[2].append(linha * coluna)

        else:
            matriz[3].append(linha * coluna)

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()