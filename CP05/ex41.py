altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / altura**2

if imc <= 18.5:
    print(f"Abaixo do peso")

elif imc >= 18.6 and imc < 25:
    print(f"Saudável")

elif imc >= 25 and imc < 30:
    print(f"Peso em excesso")

elif imc >= 30 and imc < 35:
    print("Obesidade Grau I")

elif imc >= 35 and imc < 40:
    print("Obesidade Grau II(severa)")

else:
    print("Obesidade Grau III(mórbida)")