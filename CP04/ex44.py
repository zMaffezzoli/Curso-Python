altura_degrau = float(input("Digite a altura do degrau da escada: "))
altura_desejada = float(input("Digite a altura que deseja alcançar com a escada: "))

# Não é possível subir meio degrau, logo deverá subir o degrau inteiro
print(f"Você deverá subir: {altura_desejada//altura_degrau+1}")