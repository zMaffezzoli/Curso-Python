altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo(masculino/feminino): ")
sexo = sexo.lower()

if sexo == "masculino":
    print(f"Peso ideal: {72.7 * altura - 58}")
    
else:
    print(f"Peso ideal: {32.1 * altura - 44.7}")