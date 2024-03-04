numero = int(input("Digite um número: "))

if numero > 1:
    for i in range(2, numero):
        if not numero % i:
            print(f"{numero} Não é primo")
            break
    else:
        print(f"{numero} é primo")