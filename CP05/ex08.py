nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Notas inválidas!")
    
else:
    print((nota1+nota2)/2)