inicio = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))

impares = 0

if inicio > final:
    print("Intervalo de valores inválido!")

else:
    for i in range(inicio, final+1):
        if i % 2:
            impares += 1

        else:
            pass
    
    print(f"A quantidade de número impares no intervalo é {impares}")