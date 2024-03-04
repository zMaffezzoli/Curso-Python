idade = int(input('Digite sua idade: '))
tempo_trabalhado = int(input('Digite a quantos anos você trabalha: '))

if idade >= 65 or tempo_trabalhado >= 30 or idade >= 60 and tempo_trabalhado >= 25:
    print('Pode se aposentar')

else:
    print('Não pode se aposentar')