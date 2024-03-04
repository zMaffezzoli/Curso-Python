"""
# Forma 1
from csv import writer

with open('pessoas.csv', mode='w', encoding='UTF-8', newline='') as arquivo:
    arquivo_csv = writer(arquivo)
    arquivo_csv.writerow(["Nome", "Idade"])
    nome = None

    while nome != "sair":
        nome = input("Digite um nome ('sair' p/ sair): ")
        if nome != 'sair':
            idade = input("Digite uma idade: ")
            arquivo_csv.writerow([nome, idade])"""

# Forma 2 
from csv import DictWriter

with open('pessoas.csv', mode='w', encoding='UTF-8', newline='') as arquivo:
    header = ['Nome', 'Idade']
    arquivo_csv = DictWriter(arquivo, fieldnames=header)
    arquivo_csv.writeheader()

    nome = None
    while nome != "sair":
        nome = input("Digite um nome ('sair' p/ sair): ")
        if nome != 'sair':
            idade = input("Digite uma idade: ")
            arquivo_csv.writerow({"Nome": nome, "Idade": idade})
