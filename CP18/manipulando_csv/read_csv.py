"""
# Forma 1
from csv import reader

with open('lutadores.csv', mode='r', encoding='UTF-8') as arquivo:
    read = reader(arquivo) # Retorna um interator
    next(read) # Pula o cabeçalho do arquivo
    for linhas in read:
        print(linhas)
"""
# Forma 3
from csv import DictReader

with open("lutadores.csv", mode="r", encoding="UTF-8") as arquivo:
    read = DictReader(arquivo, delimiter=",") # Delimiter é o separador dos valores
    
    for linha in read:
        print(f"{linha['Nome']}, {linha['País']}, {linha['Altura (em cm)']}")