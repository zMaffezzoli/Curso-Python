from random import randint

tentativas = 0

numero = randint(1, 1000)

while True:
    valor = int(input("Digite um valor: "))
    tentativas += 1

    if valor > numero:
        print("Chute é maior")

    elif valor < numero:
        print("Chute é menor")

    else:
        print(f"Acertou! Você levou {tentativas} tentativas")
        break