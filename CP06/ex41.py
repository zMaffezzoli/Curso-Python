while True:
    r1 = float(input("Digite o valor do primeiro resistor: "))
    r2 = float(input("Digite o valor do segundo resistor: "))

    if not(r1 * r2) / (r1 + r2):
        print("Resistência zero")
        break

    else:
        print(f"A resistência ainda não é zero")