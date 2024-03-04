from random import sample

matriz = sample(range(0, 100), 25)

linha1 = matriz[:5]
linha2 = matriz[5:10]
linha3 = matriz[10:15]
linha4 = matriz[15:20]
linha5 = matriz[20:]

matriz = [linha1] + [linha2] + [linha3] + [linha4] + [linha5]

for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna, end=" ")

    print()