valor = int(input("Digite um valor: "))

contador = 1
impar = 0

while contador <= valor:
    if (impar % 2):
        contador += 1
        print(impar)

    impar += 1