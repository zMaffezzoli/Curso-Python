valor = int(input("Digite até qual termo da série de Fibonnaci deseja: "))

fibonnaci = [0, 1, 1, 2]

ultimo = fibonnaci[-1]
penultimo = fibonnaci[-2]

if (valor == 1):
    print(fibonnaci)

else:
    for i in fibonnaci:
        fibonnaci.append(ultimo + penultimo)
        penultimo = ultimo
        ultimo = fibonnaci[-1]
        
        if fibonnaci[-1] > valor:
            break

    print(fibonnaci)