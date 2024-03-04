matriz = [[], [], [], [], []]

for i in range(len(matriz)):

    if i == 0:
        matriz[i].extend([1,0,0,0,0])

    elif i == 1:
        matriz[i].extend([0,1,0,0,0])

    elif i == 2:
        matriz[i].extend([0,0,1,0,0])

    elif i == 3:
        matriz[i].extend([0,0,0,1,0])

    else:
        matriz[i].extend([0,0,0,0,1])

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")
    
    print()