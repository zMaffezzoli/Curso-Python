from random import randint

matrizA = []
matrizB = []

for i in range(2):
    matrizA += [list(randint(1, 20) for i in range(2))]
    matrizB += [list(randint(1, 20) for i in range(2))]

print(f"1 - Somar duas matrizes \n2 - Subtrair primeira matriz da segunda \n3 - Adicionar constante as matrizes \n4 - Imprimir matrizes \n5 - Sair")

while True:

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        matrizC = [[0], [0], [0, 0, 0]]

        for linha in range(2):
            for elemento_coluna in range(2):
                matrizC[linha].insert(-1, matrizA[linha][elemento_coluna] + matrizB[linha][elemento_coluna])

    elif opcao == 2:
        matrizC = [[0], [0], [0, 0, 0]]

        for linha in range(2):
            for elemento_coluna in range(2):
                matrizC[linha].insert(-1, matrizA[linha][elemento_coluna] - matrizB[linha][elemento_coluna])

    elif opcao == 3:
        constante = int(input("Digite o valor da constante(valor inteiro): "))

        for linha in range(2):
            for elemento_coluna in range(2):
                matrizA[linha][elemento_coluna] += constante
                matrizB[linha][elemento_coluna] += constante

    elif opcao == 4:
        for linha in matrizA:
            for elemento_coluna in linha:
                print(elemento_coluna, end=" ")

            print()

        print()

        for linha in matrizB:
            for elemento_coluna in linha:
                print(elemento_coluna, end=" ")

            print()

        print()

        for linha in matrizC:
            for elemento_coluna in linha:
                print(elemento_coluna, end=" ")

            print()

        print()

    else:
        break