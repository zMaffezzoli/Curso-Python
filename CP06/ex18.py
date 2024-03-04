valor = int(input("Quantos números serão lidos: "))

maior = ""
contador = 0
for i in range(valor):
    numero = int(input("Digite um número: "))


    if i == 0:
        maior = numero
            
    if numero == maior:
        contador += 1

    if numero > maior:
        maior = numero
    

print(f"Maior número {maior}, quantidade de vezes que apareceu {contador}")