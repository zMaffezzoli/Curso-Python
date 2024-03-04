from random import randint

lista = list(randint(1, 20) for i in range(5))

while True:

    cod = int(input("Digite o código da operação: "))

    if cod == 1:
        print(lista)

    elif cod == 2:
        print(lista[::-1])

    elif cod == 0:
        break

    else:
        print("Código inválido! (Digite 1, 2 ou 0)")