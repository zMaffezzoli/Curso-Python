data = input("Digite uma data(DD/MM/AAAA): ")

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

bissexto = (not ano % 4) and bool((ano % 100))

"""
fevereiro 28 ou 29 dias
Meses 30 dias = abril. junho, setembro, novembro
Meses 31 dias = janeiro, março, maio, julho, agosto, outubro, dezembro
"""

if dia >= 1 and dia <= 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Data válida")

elif dia >= 1 and dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Data válida")

elif dia <= 28 and mes == 2:
    print("Data válida")

elif dia == 29 and bissexto:
    print("Data valida")

else:
    print("Data inválida")