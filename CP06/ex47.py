while True:
    print("1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Saída\n")
    
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 5:
        break

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    if opcao == 1:
        print(f"Adição: {valor1 + valor2}\n")

    elif opcao == 2:
        print(f"Subtração: {valor1 - valor2}\n")

    elif opcao == 3:
        print(f"Multiplicação: {valor1 * valor2}\n")

    elif opcao == 4:
        print(f"Divisão: {valor1 / valor2}\n")