valor1 = int(input("Digite o valor inicial: "))
valor2 = int(input("Digite o valor final: "))

contador = 0

for numero in range(valor1, valor2 + 1):
    if numero > 1:
        primo = True

        for i in range(2, int(numero**0.5) + 1):
            if not numero % i:
                primo = False
                break

        if primo:
            contador += 1

print(f"Existem {contador} números primos no intervalo de {valor1} até {valor2}")