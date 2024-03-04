nota1 = float(input("Digite uma nota(Considerar 0 a 100): "))
nota2 = float(input("Digite uma nota(Considerar 0 a 100): "))
nota3 = float(input("Digite uma nota(Considerar 0 a 100): "))

media = (nota1 + nota2 + nota3 * 2) / 4

if media >= 60:
    print('Aprovado')
    
else:
    print('Reprovado')