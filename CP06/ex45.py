print("1 - Conversão km/h para m/s \n2 - Conversão m/s para km/h \n3 - Sair\n")

opcao = 2

while opcao != 3:
    opcao = int(input("Digite o que deseja fazer: "))

    if opcao == 1:
        km = float(input("Digite a velocidade em km/h: "))
        print(f"km/h: {km}  m/s: {km/3.6}")

    elif opcao == 2:
        ms = float(input("Digite a velocidade em ms/s: "))
        print(f"m/s: {ms}  km/h: {ms*3.6}")

    else:
        break