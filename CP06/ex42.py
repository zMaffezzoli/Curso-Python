while True:
    valor = float(input("Digite um valor(Para parar coloque um número <= 0): "))

    if valor <= 0:
        break

    else:
        print(f"Quadrado: {valor**2}  Cubo: {valor**3}  Raiz quadrada: {valor**(1/2)}")