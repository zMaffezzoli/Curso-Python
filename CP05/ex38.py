dia = int(input("Digite o dia que você nasceu: "))
mes = int(input("Digite o mes que você nasceu: "))
ano = int(input("Digite o ano que você nasceu: "))

bissexto = (not ano % 4) and bool((ano % 100))

"""
fevereiro 28 ou 29 dias
Meses 30 dias = abril. junho, setembro, novembro
Meses 31 dias = janeiro, março, maio, julho, agosto, outubro, dezembro
"""

if dia >= 1 and dia <= 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11 and ano <= 2008:
    print("Data válida")

elif dia >= 1 and dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and ano <= 2008:
    print("Data válida")

elif dia <= 28 and mes == 2 and ano <= 2008:
    print("Data válida")

elif dia == 29 and bissexto and ano <= 2008:
    print("Data valida")

else:
    print("Data inválida")