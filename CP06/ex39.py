while True:
    base = float(input("Digite o tamanho da base do triângulo: "))
    altura = float(input("Digite o tamanho da altura do triângulo: "))

    if base <= 0 or altura <= 0:
        print("Valores inválidos!")
        continue

    else:
        print(f"A área do triângulo é: {(base*altura)/2}")
        break